from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performace_link = page.get_by_role("link", name="Performance")
        self.dasboard_link = page.get_by_role("link", name="Dashboard")
        
    def is_upgrade_button_visible(self):
        return self.upgrade_button.is_visible()
    
    def click_performance_link(self):
        self.performace_link.click()
        
    def click_dashboard_link(self):
        self.dasboard_link.click()        