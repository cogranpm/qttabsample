""" module for all models in the program """
from PySide2.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QAbstractTableModel
from PySide2.QtGui import QIcon


class NavigationItemData:
    """ is an object that is used as the data for tree navigation items """

    def __init__(self, display, icon):
        self.display = display
        self.icon = icon


class NavigationItem:
    """ is a recursive data structure (tree) """

    def __init__(self, data, parent=None):
        """ _item_data is a list of any type, 1 item for each column, parent is not required """
        self._child_items = list()
        self._parent_item = parent
        self._item_data = data

    def append_child(self, child):
        """ child is of type navigationitem """
        self._child_items.append(child)

    def child(self, row):
        """ returns a navigationitem, row is an int """
        if row < 0 or row >= len(self._child_items):
            raise IndexError
        return self._child_items[row]

    def child_count(self):
        """ returns an int """
        return len(self._child_items)

    def column_count(self):
        """ returns an int """
        return len(self._item_data)

    def data(self, column):
        """ returns a QVariant, column is an int """
        if column < 0 or column >= len(self._item_data):
            raise IndexError

        return self._item_data[column].display

    def icon(self, column):
        if self._item_data[column].icon:
            return QIcon("icons/" + self._item_data[column].icon)

    def row(self):
        """ if the current instance is not the root, """
        """ which row does the current instance occupy in the parents list of children """
        if self._parent_item:
            return self._parent_item.child_items().index(self)

        return 0

    def parent_item(self):
        """ returns a navigation item """
        if self._parent_item is None:
            return 0
        return self._parent_item

    def child_items(self):
        return self._child_items


class NavigationModel(QAbstractItemModel):
    """ is the Model class in the mvc framework for navigation items """
    """ this is the way to have a completely custom mvc model for the mvc views """

    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        root_data = NavigationItemData("Root", None)
        self._root_item = NavigationItem([root_data], None)
        # setup the model data here
        self._setup_model_data()

    def _setup_model_data(self):
        icon_id = "braindump.png"
        model_item = NavigationItem([NavigationItemData("Models", icon_id)], self._root_item)
        self._root_item.append_child(model_item)
        project_item = NavigationItem([NavigationItemData("Projects", "wrench.png")], self._root_item)
        self._root_item.append_child(project_item)
        # subitem of model
        data_model = NavigationItem([NavigationItemData("Data Model", "template.png")], model_item)
        model_item.append_child(data_model)

        # subitems of project
        timekeeping = NavigationItem([NavigationItemData("Timekeeping", "type.png")],  project_item)
        project_item.append_child(timekeeping)

        # subitems of timekeeping, just a test thing
        timecards = NavigationItem([NavigationItemData("Timecards", "wand.png")], timekeeping)
        timekeeping.append_child(timecards)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if not(index.isValid()):
            return Qt.ItemFlags.NoItemFlags
        return super().flags(index)

    def data(self, index, role):
        if not index.isValid():
            return None
        item = index.internalPointer()
        if role == Qt.ItemDataRole.DecorationRole:
            return item.icon(index.column())
        elif role == Qt.ItemDataRole.DisplayRole:
            return item.data(index.column())
        #ToolTipRole,

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self._root_item.data(section)
        return None

    def parent(self, index: QModelIndex):
        if not index.isValid():
            return QModelIndex()

        child_item: NavigationItem = index.internalPointer()
        parent_item: NavigationItem = child_item.parent_item()

        if parent_item == self._root_item:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def index(self, row, column, parent):
        """ returns QModelIndex , parent is QModelIndex type """
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self._root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if not (child_item is None):
            return self.createIndex(row, column, child_item)

        return QModelIndex()

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not(parent.isValid()):
            parent_item = self._root_item
        else:
            parent_item = parent.internalPointer()

        return parent_item.child_count()

    def columnCount(self, parent):
        if parent.isValid():
            parent_item: NavigationItem = parent.internalPointer()
            return parent_item.column_count()
        return self._root_item.column_count()


class QuestionModel(QAbstractTableModel):

    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        self.data_set = data
        self.column_count = 4
        self.row_count = len(self.data_set)


    def rowCount(self, parent=QModelIndex):
        return self.row_count

    def columnCount(self, parent=QModelIndex):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Id", "Body", "Tag", "Answer")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):

        if not index.isValid():
            return None
        column = index.column()
        row = index.row()

        #print(f"I am data-ing here, column: {column} row: {row}")
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if column == 0:
                return self.data_set[row]['id']
            elif column == 1:
                list_item = self.data_set[row]
                return list_item['body']
            elif column == 2:
                return self.data_set[row]['tag']
            elif column == 3:
                return self.data_set[row]['answer']
        # more stuff
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable )

    def setData(self, index, value, role: int = Qt.EditRole):
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.data_set):
            question = self.data_set[index.row()]
            if index.column() == 0:
                question["id"] = value
            elif index.column() == 1:
                question["body"] = value
            elif index.column() == 2:
                question["tag"] = value
            elif index.column() == 3:
                question["answer"] = value
            else:
                return False

            self.dataChanged.emit(index, index, 0)
            return True
        return False

    # todo, should we look at
    # insertRows, removeRows, setData (for editing)

    # note, we don't use this, instead each front end calls beginInsert etc
    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(index, position, position + rows - 1)
        for row in range(rows):
            self.data_set.insert(position + row, {'body': 'how to create immutable map in python', 'tag': 'collections',
                              'answer': 'there is no way to do it'})
        #self.data_set.append({'body': 'how to create immutable map in python', 'tag': 'collections', 'answer': 'there is no way to do it'})
        self.endInsertRows()
        #return QAbstractTableModel.insertRows(self, row, count, index)
        return True

    # def insertRow(self, row, index=QModelIndex()):
    #     self.beginInsertRows(index, row, row)
    #     self.data_set.append({'body': 'how to create immutable map in python', 'tag': 'collections',
    #                           'answer': 'there is no way to do it'})
    #     self.endInsertRows()
    #     return True

