from datetime import datetime

import littletable as lt
import pyparsing as pp
import pyperclip as pc

clip = pc.paste()
if not clip:
    print("must copy Amazon ranking stats to the clipboard")
    import sys; sys.exit(0)

# print(clip)

# parser to extract fields from Amazon rankings output:
#   Best Sellers Rank: #75,543 in Books (See Top 100 in Books)
#      #34 in Data Processing
#      #86 in Python Programming
#      #112 in Software Development (Books)
"""
Best Sellers Rank: #96,193 in Books (See Top 100 in Books)
#54 in Data Processing
#92 in Python Programming
#99 in Software Development (Books)
Customer Reviews: 4.8 4.8 out of 5 stars    9 ratings
"""

rank = "#" + pp.Word(pp.nums, pp.nums+",")
rank.add_parse_action(lambda t: int(t[1].replace(',', '')))

ranks_data = (
    "Best Sellers Rank:" + rank("all_books_rank") + "in Books (See Top 100 in Books)"
    + ((rank("data_processing_rank") + "in Data Processing")
       & (rank("python_rank") + "in Python Programming")
       & (rank("software_development_rank") + "in Software Development (Books)"))
)
reviews_data = (
        pp.Literal("Customer Reviews:") + ... + (pp.common.integer("total_ratings") + "ratings")
)

parsed = (ranks_data + reviews_data).parse_string(clip)

if parsed:
    rankings_file = "pian_amazon_rankings.csv"

    ranks_db = lt.Table().csv_import(rankings_file)

    # copy ratings info from last entry in CSV - edit these manually, not from clipboard
    last = ranks_db[-1]
    ratings_cols = "star_5,star_4,star_3,star_2,star_1".split(",")

    # build a ParseResults as if this were parsed from the clipboard
    ratings_pr = pp.ParseResults.from_dict({col: getattr(last, col) for col in ratings_cols})
    # print(ratings_pr.dump())
    parsed += ratings_pr

    # add new data to CSV
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
    attr = "total_ratings"
    last_total_ratings = int(getattr(last, attr))
    cur_total_ratings = int(getattr(current, attr))
    print(f"Total ratings: {current.total_ratings}"
          f" ({last_total_ratings - cur_total_ratings:+,})"
          f" {'<UPDATE RATINGS>' if (last_total_ratings != cur_total_ratings) else ''}"
          )

    # for i in range(5, 0, -1):
    #     cur_stars = int(getattr(current, 'star_' + str(i)))
    #     prv_stars = int(getattr(last, 'star_' + str(i)))
    #     print(f"       {i} star: {cur_stars} ({cur_stars - prv_stars:+,})")

else:
    print("must copy Amazon ranking stats to the clipboard")
