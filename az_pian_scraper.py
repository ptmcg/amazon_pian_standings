from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyparsing as pp
import littletable as lt
from datetime import datetime


def get_browser_page_source(url: str) -> str:
    driver_path = "chromedriver.exe"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=webdriver.chrome.service.Service(driver_path),
        options=options,
    )
    page_source = ""
    try:
        driver.get(url)
        page_source = driver.page_source
    except Exception:
        pass
    finally:
        driver.quit()

    return page_source


html_sample = """
<span class="a-text-bold"> Best Sellers Rank: </span> #204,352 in Books (<a href="/gp/bestsellers/books/ref=pd_zg_ts_books">
See Top 100 in Books</a>) 
<ul class="a-unordered-list a-nostyle a-vertical zg_hrsr">  
<li><span class="a-list-item"> #136 in <a href="/gp/bestsellers/books/10806588011/ref=pd_zg_hrsr_books">Data Processing</a></span></li>  
<li><span class="a-list-item"> #218 in <a href="/gp/bestsellers/books/285856/ref=pd_zg_hrsr_books">Python Programming</a></span></li>  
<li><span class="a-list-item"> #337 in <a href="/gp/bestsellers/books/4016/ref=pd_zg_hrsr_books">Software Development (Books)</a></span></li>  
</ul>
</span>

<div class="a-popover-content" id="a-popover-content-4"><div class="a-fixed-left-grid"><div class="a-fixed-left-grid-inner" style="padding-left:300px"><div class="a-fixed-left-grid-col a-col-left" style="width:300px;margin-left:-300px;float:left;"><div class="a-icon-row a-spacing-small a-padding-none"><i data-hook="average-stars-rating-anywhere" class="a-icon a-icon-star a-star-5"><span class="a-icon-alt">5 out of 5</span></i><span data-hook="acr-average-stars-rating-text" class="a-size-medium a-color-base a-text-beside-button a-text-bold">5 out of 5</span></div><div class="a-row a-spacing-medium"><span data-hook="total-review-count" class="a-size-base a-color-secondary totalRatingCount">2 global ratings</span></div>

<table id="histogramTable" class="a-normal a-align-center a-spacing-base">

    <tbody><tr data-reftag="" data-reviews-state-param="{&quot;filterByStar&quot;:&quot;five_star&quot;, &quot;pageNumber&quot;:&quot;1&quot;}" aria-label="5 stars represent 100% of rating" class="a-histogram-row a-align-center">

      <td class="aok-nowrap">
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal 5star" title="5 stars represent 100% of rating" href="/product-reviews/1098113551/ref=acr_dpx_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
            5 star
          </a>
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td class="a-span10">
        <a aria-disabled="true" class="a-link-normal" title="5 stars represent 100% of rating" href="/product-reviews/1098113551/ref=acr_dpx_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">
          <div class="a-meter" role="progressbar" aria-valuenow="100%"><div class="a-meter-bar a-meter-filled" style="width: 100%;"></div></div>
        </a>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>
        <span class="a-size-base">
          <a aria-disabled="true" class="a-link-normal" title="5 stars represent 100% of rating" href="/product-reviews/1098113551/ref=acr_dpx_hist_5?ie=UTF8&amp;filterByStar=five_star&amp;reviewerType=all_reviews#reviews-filter-bar">

              100%

          </a>
        </span>
      </td>
    </tr>

    <tr class="a-histogram-row">

      <td class="a-nowrap">
        <span class="a-size-base">
          4 star
        </span>


        <span class="a-offscreen">
          0% (0%)
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td aria-hidden="true" class="a-span10">
        <div class="a-meter" role="progressbar" aria-valuenow="0%"><div class="a-meter-bar a-meter-filled" style="width: 0%;"></div></div>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>

        <span class="a-size-base">

            0%

        </span>
      </td>
    </tr>

    <tr class="a-histogram-row">

      <td class="a-nowrap">
        <span class="a-size-base">
          3 star
        </span>


        <span class="a-offscreen">
          0% (0%)
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td aria-hidden="true" class="a-span10">
        <div class="a-meter" role="progressbar" aria-valuenow="0%"><div class="a-meter-bar a-meter-filled" style="width: 0%;"></div></div>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>

        <span class="a-size-base">

            0%

        </span>
      </td>
    </tr>

    <tr class="a-histogram-row">

      <td class="a-nowrap">
        <span class="a-size-base">
          2 star
        </span>


        <span class="a-offscreen">
          0% (0%)
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td aria-hidden="true" class="a-span10">
        <div class="a-meter" role="progressbar" aria-valuenow="0%"><div class="a-meter-bar a-meter-filled" style="width: 0%;"></div></div>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>

        <span class="a-size-base">

            0%

        </span>
      </td>
    </tr>

    <tr class="a-histogram-row">

      <td class="a-nowrap">
        <span class="a-size-base">
          1 star
        </span>


        <span class="a-offscreen">
          0% (0%)
        </span>

        <span class="a-letter-space"></span>
      </td>

      <td aria-hidden="true" class="a-span10">
        <div class="a-meter" role="progressbar" aria-valuenow="0%"><div class="a-meter-bar a-meter-filled" style="width: 0%;"></div></div>
      </td>

      <td class="a-text-right a-nowrap">
        <span class="a-letter-space"></span>

        <span class="a-size-base">

            0%

        </span>
      </td>
    </tr>

</tbody></table>
<hr aria-hidden="true" class="a-spacing-large a-divider-normal"><div class="a-section a-spacing-base a-text-center"><a class="a-size-base a-link-emphasis" href="/dp/1098113551#customerReviews">See all customer reviews</a></div></div></div></div></div>
"""
html_sample = """

"""
if 1:
    print("getting page source")
    html = get_browser_page_source(
        "https://www.amazon.com/Python-Nutshell-Desktop-Quick-Reference/dp/1098113551"
    )
else:
    html = html_sample


span, end_span = map(pp.Suppress, pp.make_html_tags("span"))
a, end_a = map(pp.Suppress, pp.make_html_tags("a"))
li, end_li = map(pp.Suppress, pp.make_html_tags("li"))
ul, end_ul = map(pp.Suppress, pp.make_html_tags("ul"))
rank = "#" + pp.Word(pp.nums, pp.nums+",")
rank.add_parse_action(lambda t: int(t[1].replace(',', '')))

ranks_data = (
    "Best Sellers Rank:" + end_span
    + rank("all_books_rank") + "in Books (" + a + "See Top 100 in Books" + end_a + ")"
    + ul
    + li + span + rank("data_processing_rank") + "in" + a + "Data Processing" + end_a + end_span + end_li
    + li + span + rank("python_rank") + "in" + a + "Python Programming" + end_a + end_span + end_li
    + li + span + rank("software_development_rank") + "in" + a + "Software Development (Books)" + end_a + end_span + end_li
    + end_ul
)


integer = pp.common.integer
total_review_count_span = pp.make_html_tags("span")[0].add_parse_action(pp.with_attribute(**{"data-hook": "total-review-count"}))

global_count = integer("total_ratings") + "global ratings"

star_header_span = pp.make_html_tags("span")[0].add_parse_action(pp.with_attribute(**{"class": "a-size-base"}))
star_header = star_header_span.suppress() + pp.Opt(a.suppress()) + integer("star_count") + "star" + pp.Opt(end_a.suppress()) + end_span
star_percent_span = pp.make_html_tags("span")[0].add_parse_action(pp.with_attribute(**{"class": "a-offscreen"}))

star_count = star_header_span.suppress() + pp.Opt(a.suppress()) + integer("star_percent") + "%" + pp.Opt(end_a.suppress()) + end_span

star_count_section = star_header + ... + star_count
star_count_section.add_parse_action(lambda t: t.__delitem__("_skipped") or t.__delitem__(1))

print("parsing fetched HTML")
parsed = ranks_data.search_string(html, max_matches=1)
if parsed:
    rankings_file = "pian_amazon_rankings.csv"
    parsed: pp.ParseResults = parsed[0]

    ranks_db = lt.Table().csv_import(rankings_file)
    last = ranks_db[-1]

    all_reviews = global_count.search_string(html, max_matches=1)

    total_stars = all_reviews[0].total_ratings
    all_stars = star_count_section.search_string(html, max_matches=5)

    parsed += all_reviews[0]
    for star_result in all_stars:
        num_stars = int(star_result.star_percent / 100 * total_stars)
        parsed[f"star_{star_result.star_count}"] = num_stars
    # print(parsed.dump())
    # del parsed["_skipped"]

    # for attr, val in zip("total_ratings,star_5,star_4,star_3,star_2,star_1".split(","), (2, 2, 0, 0, 0, 0)):
    #     parsed[attr] = val

    ranks_db.insert(
        {
            "timestamp": f"{datetime.now():%Y-%m-%d %H:%M:%S}",
            **parsed.as_dict()
        }
    )
    ranks_db.csv_export(rankings_file)
    current = ranks_db[-1]

    # print deltas from last time
    print()
    for category in "all_books data_processing python software_development".split():
        attr = f"{category}_rank"
        print(f"{category.replace('_', ' ').title()}: {int(getattr(current, attr)):,}"
              f" ({int(getattr(last, attr)) - int(getattr(current, attr)):+,})")
    print()
    print(f"Total ratings: {current.total_ratings}")
    for i in range(5, 0, -1):
        cur_stars = int(getattr(current, 'star_' + str(i)))
        prv_stars = int(getattr(last, 'star_' + str(i)))
        print(f"       {i} star: {cur_stars} ({cur_stars - prv_stars:+,})")

else:
    print("No rankings found in page")
    print(html)
