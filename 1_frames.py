import ttkbootstrap as tb
import requests as req
from ttkbootstrap.constants import *
from k import *


class SearchBar(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=(0, PM), fill=BOTH, expand=True)

        self.label_text = tb.StringVar(value='No search results')

        self.search_bar = tb.Entry(self, font=BODY)
        self.search_button = tb.Button(self, text='Search', command=self.get_records)
        self.search_results_label = tb.Label(self, textvariable=self.label_text, font=LEAD, justify=CENTER)

        self.search_results_label.pack(expand=True, padx=PM, pady=PM, side=BOTTOM)
        self.search_bar.pack(side=LEFT, fill=X, expand=True)
        self.search_button.pack(side=LEFT, padx=(PXS, 0))

    def get_records(self):
        #self.label_text.set(value='SMIC')
        name = self.search_bar.get()
        if len(name) < 1:
            self.label_text.set(value='ERROR\nNo Query Given')
        else:
            url_string = f'http://10.6.21.76:8000/academics/{name}'
            response = req.get(url_string).json()
            if 'msg' in response:
                self.label_text.set(value=response['msg'])
            else:
                response_string = f"""
                Name: {response['name']}
                Grade: {response['name']}
                GPA: {response['gpa']}
                """
                self.label_text.set(value=response_string)

class ButtonGroup(tb.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=PM, pady=PM, fill=X)

        self.submit_button = tb.Button(self, text='submit', bootstyle=SUCCESS)
        self.cancel_button = tb.Button(self, text='cancel', bootstyle=(OUTLINE, SECONDARY))

        self.submit_button.pack(side=RIGHT)
        self.cancel_button.pack(side=RIGHT)

class AcademicSearchWindow(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True, fill=BOTH)

        subtitle = 'A great tool for searching academic records and more importantly, failures.'

        self.title_label = tb.Label(self, bootstyle=PRIMARY, font=H1, text='SMIC ACADEMIC RECORDS')
        self.subtitle_label = tb.Label(self, text=subtitle, font=LEAD)

        self.title_label.pack(padx=PM, pady=(PM, PS), anchor=W)
        self.subtitle_label.pack(padx=PM, pady=(0, PM), anchor=W)
        self.search_bar = SearchBar(self)

class AthleticSearchWindow(tb.Frame):

    def __init__(self, master):
        super().__init__(master)
        #self.pack(expand=True, fill=BOTH)

        subtitle = 'A great tool for searching athletic records.'

        self.title_label = tb.Label(self, bootstyle=PRIMARY, font=H1, text='SMIC Athletic RECORDS')
        self.subtitle_label = tb.Label(self, text=subtitle, font=LEAD)

        self.title_label.pack(padx=PM, pady=(PM, PS), anchor=W)
        self.subtitle_label.pack(padx=PM, pady=(0, PM), anchor=W)
        self.search_bar = SearchBar(self)

class App(tb.Window):
    def __init__(self):
        super().__init__(themename='darkly')

        self.title('Frames')
        self.geometry('1920x1080')

        self.nav_frame = tb.Frame(self, bootstyle=PRIMARY)
        self.nav_frame.pack(fill=X, ipadx=PXS, ipady=PXS)

        self.container = tb.Frame(self)
        self.container.pack(fill=BOTH, expand=True)

        self.academic_button = tb.Button(
            self.nav_frame,
            text='Academic Records',
            bootstyle=SECONDARY,
            command=lambda: self.change_frame(name='academic')
        )
        self.athletic_button = tb.Button(
            self.nav_frame,
            text='Athletic Records',
            bootstyle=SECONDARY,
            command=lambda: self.change_frame(name='athletic')
        )

        self.athletic_button.pack(side=RIGHT, padx=PXS)
        self.academic_button.pack(side=RIGHT, padx=PXS)

        self.frames = {
            'academic': AcademicSearchWindow(self.container),
            'athletic': AthleticSearchWindow(self.container),
        }

        self.current_frame = 'academic'
        self.set_frame()

    def set_frame(self):
        self.frames[self.current_frame].pack(fill=BOTH, expand=True)

    def remove_frame(self):
        self.frames[self.current_frame].pack_forget()

    def change_frame(self, name):
        self.remove_frame()
        self.current_frame = name
        self.set_frame()


if __name__ == '__main__':
    app = App()
    app.place_window_center()
    app.mainloop()
