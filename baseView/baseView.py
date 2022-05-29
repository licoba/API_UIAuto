class BaseView(object):
    """封装元素操作"""
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elemets(self,*loc):
        return self.find_elemets(*loc)

    def get_window_size(self):
        return self.driver.get_windows_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(self,start_x,start_y,end_x,end_y,duration)


