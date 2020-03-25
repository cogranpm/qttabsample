from PySide2.QtCore import QModelIndex, QObject, Qt, QAbstractTableModel
from collections import namedtuple

HeaderSpec = namedtuple('HeaderSpec', ['fieldname', 'title'])

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
            column = index.column()
            question[self.headerspec[column].fieldname] = value
            self.dataChanged.emit(index, index, 0)
            return True
        return False

    # how is this done in a model agnostic manner
    #def insertRows(self, row, count, index):
    #    self.beginInsertRows(index, row, row + count - 1)
    #    self.endInsertRows()
    #    return True



