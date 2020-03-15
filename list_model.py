from PySide2.QtCore import QModelIndex, QObject, Qt, QAbstractTableModel


class ListModel(QAbstractTableModel):

    # headerspec is a list of namedtuples
    def __init__(self, data=None, headerspec=None):
        QAbstractTableModel.__init__(self)
        self.data_set = data
        self.headerspec = headerspec
        self.column_count = len(self.headerspec)
        self.row_count = len(self.data_set)

    def rowCount(self, parent=QModelIndex):
        return self.row_count

    def columnCount(self, parent=QModelIndex):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.headerspec[section].title
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):

        if not index.isValid():
            return None
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.data_set[row][self.headerspec[column].fieldname]
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




