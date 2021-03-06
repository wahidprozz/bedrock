# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.ios_hub import FirefoxIOSHubPage


@pytest.mark.smoke
@pytest.mark.nondestructive
def test_app_store_button_is_displayed(base_url, selenium):
    page = FirefoxIOSHubPage(selenium, base_url).open()
    assert page.is_app_store_button_displayed


@pytest.mark.nondestructive
def test_news_feed_is_displayed(base_url, selenium):
    page = FirefoxIOSHubPage(selenium, base_url).open()
    assert len(page.news_feed.articles) == 3
