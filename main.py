import sys

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

from atelie_templates.manager_template.atelie_manager import Ui_MainWindow
from atelie_templates.add_template.add_item import Ui_Dialog as Add_Dialog
from atelie_templates.edit_template.edit_item import Ui_Dialog as Edit_Dialog
from atelie_templates.results_template.result import Ui_Dialog as Result_Dialog

from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QErrorMessage
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtGui import QKeyEvent

from styles import changeTheme

engine = create_engine('sqlite:///atelie.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class AtelieProducts(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    cost = Column(Float)

Base.metadata.create_all(engine)


class BaseWindow:
    eqPressed = Signal()

    def __init__(self) -> None:
        pass

    def _connectButton(self, button, slot):
        button.clicked.connect(slot)

    def _makeSlot(self, function, *args, **kwargs):
        def realSlot():
            function(*args, **kwargs)

        return realSlot

    def _checkAndEmit(self, key, signal: Signal, *args):
        if key:
            signal.emit(*args)
    

class ResultDialog(Result_Dialog, QDialog, BaseWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Resultado')

        self._buttonPressed()

    def _buttonPressed(self):
        self._connectButton(self.pushButton, self._sendButtons)
    
    def _sendButtons(self, button): 
        self.close()


class AddDialog(Add_Dialog, QDialog, BaseWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Adicione um produto')

        self._mainWindow = None
        self._editDialog = None

        self._buttonPressed()
    
    @property
    def mainWindow(self):
        return self._mainWindow
    
    @mainWindow.setter
    def mainWindow(self, window):
        self._mainWindow = window

    @property
    def editDialog(self):
        return self._editDialog
    
    @editDialog.setter
    def editDialog(self, dialog):
        self._editDialog = dialog

    def _buttonPressed(self):
        self._connectButton(self.buttonBox, self._sendButtons)

    def _sendButtons(self, button):
        if not button:
            return

        if button.text() == "Cancel":
            self.close()
            return        
        
        self._createProduct()

        self.close()

    def _createProduct(self):
        if self.productName is None or self.productName.text() == '':
            return

        if self.productCost is None or self.productCost.text() == '':
            return

        if self.productPrice is None or self.productCost.text() == '':
            return

        try:
            productName = self.productName.text()
            productCost = float(self.productCost.text())
            productPrice = float(self.productPrice.text())

            if productCost > productPrice:
                return

            item = AtelieProducts(name=productName, price=productPrice, cost=productCost)
            session.add(item)
            session.commit()

            self.mainWindow.updateInfo()
            self.editDialog.updateInfo()

        except:
            raise('Coloque apenas o preço.')

        finally:
            self.productName.setText('')
            self.productPrice.setText('')
            self.productCost.setText('')

class EditDialog(Edit_Dialog, QDialog, BaseWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Edite seus produtos')

        self.updateInfo()

        self._buttonPressed()
    
    def _buttonPressed(self):
        self._connectButton(self.buttonBox, self._sendButtons)

    def _sendButtons(self, button):
        if not button:
            return

        if button.text() == "Cancel":
            self.close()
            return        

        self._editInfo()
        self.close()

    def updateInfo(self):
        self.productName.clear()

        queryProducts = session.query(AtelieProducts).all()
        for product in queryProducts:
            self.productName.addItem(product.name)

    @Slot()
    def _editInfo(self):
        currentProduct = self.productName.currentText()
        
        if currentProduct is None or currentProduct == '':
            return

        if self.newPrice.text() is None or self.newPrice.text() == '':
            return

        if self.newCost.text() is None or self.newCost.text() == '':
            return
            
        product = session.query(AtelieProducts).filter_by(name=currentProduct).first()

        try:
            cost = float(self.newCost.text())
            price = float(self.newPrice.text())
            
            if cost is None or cost == 0:
                cost = product.cost

            if price is None or price == 0:
                price = product.price
            
            product.cost = cost
            product.price = price
            session.commit()

        except:
            raise('Preencha corretamente os campos')

        finally:
            self.productName.setCurrentText('')
            self.newCost.setText('')
            self.newPrice.setText('')

class MainWindow(Ui_MainWindow, QMainWindow, BaseWindow):
    def __init__(self, addDialog: AddDialog, editDialog: EditDialog, resultDialog: ResultDialog) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Calcule seu fluxo de caixa!')

        self._addDialog = addDialog
        self._editDialog = editDialog
        self._resultDialog = resultDialog

        self.updateInfo()

        self._sendButtons()

    def _sendButtons(self):
        openAddDialogSlot = self._makeSlot(self._openAddDialog, self.addButton)
        self._connectButton(self.addButton, openAddDialogSlot)

        openEditDialogSlot = self._makeSlot(self._openEditDialog, self.editButton)
        self._connectButton(self.editButton, openEditDialogSlot)

        sendButtonSlot = self._makeSlot(self._calculate, self.sendButton)
        self._connectButton(self.sendButton, sendButtonSlot)

        self.eqPressed.connect(self._calculate)

    @Slot()
    def _openAddDialog(self, buttonSignal):
        if not buttonSignal:
            return

        self._openDialog(self._addDialog)

    @Slot()
    def _openEditDialog(self, buttonSignal):
        if not buttonSignal:
            return

        self._openDialog(self._editDialog)

    @Slot()
    def _calculate(self, *args):
        try:
            product = session.query(AtelieProducts).filter_by(name=self.productsBox.currentText()).first()
            
            quantity = float(self.quantityProducts.text())
            percentage = float(self.discountPercentage.text())

            totalPrice = product.price * quantity

            discount = totalPrice * (percentage / 100)
            priceWithDiscount = totalPrice - discount

            cost = product.cost * quantity

            profit = priceWithDiscount - cost

            self._resultDialog.incomeLabel.setText(str(totalPrice))
            self._resultDialog.priceLabel.setText(str(priceWithDiscount))
            self._resultDialog.costLabel.setText(str(cost))
            self._resultDialog.discountLabel.setText(str(discount))
            self._resultDialog.profitLabel.setText(str(profit))

            self._resultDialog.show()
        
        except:
            pass
        
        finally:
            self.quantityProducts.clear()
            self.discountPercentage.clear()
            self.productsBox.setCurrentText('')

    def updateInfo(self):
        self.productsBox.clear()

        queryProducts = session.query(AtelieProducts).all()
        for product in queryProducts:
            self.productsBox.addItem(product.name)

    def _openDialog(self, dialog: AddDialog | EditDialog):
        dialog.show()

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]

        self._checkAndEmit(isEnter, self.eqPressed)
        return super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    addDialog = AddDialog()
    editDialog = EditDialog()
    resultDialog = ResultDialog()
    window = MainWindow(addDialog=addDialog, editDialog=editDialog, resultDialog=resultDialog)

    addDialog.mainWindow = window
    addDialog.editDialog = editDialog

    changeTheme()

    window.show()
    app.exec()
