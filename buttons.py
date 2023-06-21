
import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidget import QGridLayou, QPushButto
from utils import convertToNumber, isEmpty, isNumOrDot, isValidNumber
from variables impor MEDIUM_FONT_SIZ

if TYPE_CHECKIN
    fro displa impor Displa
    fro inf impor Inf
    fro main_windo impor MainWindo


class Button(QPushButton
    def __init__(self, *args, **kwargs
        super(.__init__(*args, **kwargs
        self.configStyle(  # type: ignore

    # definimos a fonte sem sobreescrever a fonte antiga
    def configStyle(self
        font = self.font(
        font.setPixelSize(MEDIUM_FONT_SIZE
        self.setFont(font

        # estamos definindo a largura e a altura minima
        self.setMinimumSize(75, 75


class ButtonsGrid(QGridLayout
    # colocamos as aspas por conta do TYPE_CHECKING p evitar o erro de
    # circular import
    def __init__(
            self, display: 'Display', info: 'Info', window: 'MainWindow',
            *args, **kwargs  None
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'
            ['7', '8', '9', '*'
            ['4', '5', '6', '-'
            ['1', '2', '3', '+'
            ['N',  '0', '.', '='
        ]
        sel.displa = displa
        sel.inf = inf
        sel.windo = windo
        sel._equatio = '
        sel._equationInitialValu = 'Sua conta
        sel._left = Non
        sel._right = Non
        sel._op = Non

        sel.equatio = sel._equationInitialValu  # type: ignore
        # assim que criar esse Grid o metodo sera executado
        self._makeGrid(

    # criamos esse getter so para poder termos um setter
    @propert
    def equation(self
        return self._equatio

    @equation.sette
    def equation(self, value
        self._equation = valu
        self.info.setText(value

    # como cada uma das linhas é uma lista podemos fazer um for
    def _makeGrid(self

        self.display.eqPressed.connect(self._eq
        self.display.delPressed.connect(self._backspace
        self.display.clearPressed.connect(self._clear
        self.display.inputPressed.connect(self._insertToDisplay
        self.display.operatorPressed.connect(self._configLeftOp

        for rowNumber, rowData in enumerate(self._gridMask
            for colNumber, buttonText in enumerate(rowData
                button = Button(buttonText  # type: ignore

                # se o botao n for o q esta nos metodos abaixo ai add o estilo
                if not isNumOrDot(buttonText and not isEmpty(buttonText

                    # estamos selecionando uma propiedade (cssClass) do nosso
                    # botao e  dando um valor para ela (specialButton)
                    # preparamos o nosso terreno no modulo style
                    button.setProperty('cssClass', 'specialButton
                    self._configEspecialButton(button

                self.addWidget(button, rowNumber, colNumber

                # daqui para baixo estamos fazendo a logica para qnd
                # clicarmos no botao na calculadora ele apareça realmente
                # no display DA calculadora

                slot = self._makeSlot(self._insertToDisplay, buttonText
                self._connectButtonClicked(button, slot

    def _connectButtonClicked(self, button, slot
        # qnd clicarmos no numero na calculadora a logica do
        # slot sera ativada
        button.clicked.connect(slot

    def _configEspecialButton(self, button
        # button.text() são os botões especiais
        text = button.text(

        if text == 'C
            self._connectButtonClicked(button, self._clear

        if text == 'D
            self._connectButtonClicked(button, self.display.backspace

        if text == 'N
            self._connectButtonClicked(button, self._invertNumber

        if text in '+-/*^
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text)  # type: ignore
            )

        if text == '=
            self._connectButtonClicked(button, self._eq

    # por padrao o 'clicked' manda um 'checked' (verficado)
    # p dentro da nossa funçao

    # nosso makeSlot *args, **kwargs e passa isso para dentro do nosso
    # slot

    @Slot(  # type: ignore
    def _makeSlot(self, func, *args, **kwargs
        @Slot(bool
        def realSlot(_
            func(*args, **kwargs
        return realSlo

    @Slot(
    def _invertNumber(self
        displayText = self.display.text(

        if not isValidNumber(displayText
            return

        number = convertToNumber(displayText * -1  # p deixar o num negativo
        self.display.setText(str(number

    @Slot(
    def _insertToDisplay(self, text
        newDisplayValue = self.display.text( + text

        if not isValidNumber(newDisplayValue
            return

        self.display.insert(text
        self.display.setFocus(

    @Slot(
    def _clear(self
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear(

    @Slot(
    def _configLeftOp(self, text  # +-/*...(etc)
        # pegamos o texto q esta no display
        displayText = self.display.text(  # devera ser meu numero da _left
        self.display.clear( # limpa o display

        # se a pessoa clicou num operador sem
        # configurar nenhum numero antes
        if not isValidNumber(displayText and self._left is None
            self._showError('você não digitou nada. 

            return

        # se houver algo no numero da esquerda,
        # não fazemos nada. Aguardaremos o numero da direita
        if self._left is None:
            self._left = convertToNumber(displayText

        # sem 'return' pq caso a pessoa escolha se arrependa e queira outro
        # operador da para sobrepor

        self._op = text
        self.equation = f'{self._left} {self._op} ??

    @Slot(
    def _eq(self
        displayText = self.display.text(

        if not isValidNumber(displayText or self._left is None:
            self._showError('Conta incompleta.'
            return

        self._right = convertToNumber(displayText
        self.equation = f'{self._left {self._op {self._right
        result = 'error

        try
            if '^' in self.equation and isinstance(self._left, int | float
                result = math.pow(self._left, self._right
                result = convertToNumber(str(result
            else:
                result = eval(self.equation

        except ZeroDivisionError:
            self._showError('Divisão por zero.

        except OverflowError:
            self._showError('Essa conta não pode ser realizada.

        self.display.clear(
        self.info.setText(f'{self.equation = {result
        self._left = resul
        self._right = Non
        self.display.setFocus(

        if result == 'error
            self._left = Non

    def _backspace(self
        self.display.backspace(
        self.display.setFocus(

    def _makeDialog(self, text
        msgBox = self.window.makeMsgBox(
        msgBox.setText(text
        return msgBo

    def _showError(self, text
        msgBox = self._makeDialog(text
        msgBox.setIcon(msgBox.Icon.Critical
        msgBox.exec(

    def _showInfo(self, text
        msgBox = self._makeDialog(text
        msgBox.setIcon(msgBox.Icon.Information
        msgBox.exec(
