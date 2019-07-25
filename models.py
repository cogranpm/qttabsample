""" module for all models in the program """
from PySide2.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt
from PySide2.QtGui import QIcon


class NavigationItem:
    """ is a recursive data structure (tree) """

    def __init__(self, data, parent=None, icon=None):
        """ _item_data is a list of any type, 1 item for each column, parent is not required """
        self._child_items = list()
        self._parent_item = parent
        self._item_data = data
        self._icon_id = icon

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

        return self._item_data[column]

    def icon(self):
        if self._icon_id:
            return QIcon("icons/" + self._icon_id)

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
        self._root_item = NavigationItem(["Root"], None, None)
        # setup the model data here
        self._setup_model_data()

    def _setup_model_data(self):
        icon_id = "braindump.png"
        model_item = NavigationItem(["Models"], self._root_item, icon_id)
        self._root_item.append_child(model_item)
        project_item = NavigationItem(["Projects"], self._root_item, icon_id)
        self._root_item.append_child(project_item)
        # subitem of model
        data_model = NavigationItem(["Data Model"], model_item, icon_id)
        model_item.append_child(data_model)

        # subitems of project
        timekeeping = NavigationItem(["Timekeeping"], project_item, icon_id)
        project_item.append_child(timekeeping)

        # subitems of timekeeping, just a test thing
        timecards = NavigationItem(["Timecards"], timekeeping, icon_id)
        timekeeping.append_child(timecards)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if not(index.isValid()):
            return Qt.ItemFlags.NoItemFlags

        return super().flags(index)



        #return super().flags(index)

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()
        if role == Qt.ItemDataRole.DecorationRole:
            return item.icon()
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
