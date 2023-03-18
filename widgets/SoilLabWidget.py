from PySide6.QtWidgets import (QTabWidget)

from tabs.GeneralInfoTab import GeneralInfoTab
from tabs.SoilCorrosionTab import SoilCorrosionTab
from tabs.MainTab import MainTab

import pandas as pd


class SoilLabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._tabs = []
        self._tabs.append(MainTab())
        # self._tabs.append(GeneralInfoTab())
        # self._tabs.append(SoilCorrosionTab())
        for t in self._tabs:
            self.addTab(t, t.title)

    def import_from_excel(self, filename):
        for t in self._tabs:
            df = pd.read_excel(filename, sheet_name=t.title, index_col=0)
            t.load_data_to_model(df.to_dict(orient='list'))

        # try:
        #     f = open(filename, "rb")
        # except IOError:
        #     QMessageBox.information(self, f"Не удалось открыть файл: {filename}")
        # finally:
        #     f.close()

    def export_to_excel(self, filename):
        # headers = []
        # values = []
        # dfs = []
        sheets = {}

        for t in self._tabs:
            # headers.append(t.get_headers_to_write_in_file())
            # print(headers)
            # values.append(t.get_values_to_write_in_file())
            # print(values)
            title = t.title
            sheets.update({title: pd.DataFrame(data=t.get_values_to_write_in_file(),
                                               columns=t.get_headers_to_write_in_file())})
            sheets[title].index.name = "№ п/п"
            sheets[title].index += 1
            # sheets[title].columns = pd.MultiIndex.from_arrays([t.get_headers_to_write_in_file()])
            # print(sheets[title].to_numpy())
            # print(sheets[title].columns)
            # print(sheets[title])

        # headers = ["Наименование объекта", "Дата"]
        # values = ["Тестовый объект", "2022-10-27"]
        # sheets.update({"Лаб объект": pd.DataFrame({"Наименование объекта": ["Тестовый объект"],
        #                                            "Дата": ["2022-10-27"]})})

        writer = pd.ExcelWriter(filename + '.xlsx', engine='xlsxwriter')
        for sheet_name in sheets.keys():
            sheets[sheet_name].to_excel(writer, sheet_name=sheet_name)
            # worksheet = writer.sheets[sheet_name]
            # for col_num, value in enumerate(sheets[sheet_name].columns.values):
            #     worksheet.write(0, col_num, value)

        writer.close()
