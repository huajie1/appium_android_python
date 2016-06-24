package com.huajie.uidemo;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiScrollable;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class Demo extends UiAutomatorTestCase{
	
	public void testDemo() throws UiObjectNotFoundException{
		UiObject setting = new UiObject(new UiSelector().text("设置"));
		setting.clickAndWaitForNewWindow();
		UiScrollable settingListView = new UiScrollable(new UiSelector().className("android.widget.ScrollView"));
		UiObject aboutMobile = new UiObject(new UiSelector().text("关于手机"));
		settingListView.scrollIntoView(aboutMobile);
		aboutMobile.clickAndWaitForNewWindow();

	}


}
