from playwright.sync_api import Page

class WebComponent:
  
  def __init__(self, page: Page, html: str = '', styles: str = ''):
    self.__html = html
    self.__styles = styles
    self.__page = page
  
  @property
  def Html(self):
    return self.__html

  @property
  def Styles(self):
    return self.__styles

  @Html.setter
  def Html(self, new_html: str):
    self.__html = new_html

  @Styles.setter
  def Styles(self, new_styles: str):
    self.__styles = new_styles

  def render():
    pass
  
  def get_image(self):
    self.render()
    self.__page.set_content(self.__html)
    self.__page.add_style_tag(content=self.__styles)
    return self.__page.screenshot()
