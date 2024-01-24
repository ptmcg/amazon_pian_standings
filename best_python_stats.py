import littletable as lt
from datetime import date
from itertools import takewhile

int_fields = "all_books_rank,data_processing_rank,python_rank,software_development_rank,total_ratings,star_5,star_4,star_3,star_2,star_1".split(",")
stats = lt.Table().csv_import("pian_amazon_rankings.csv", transforms={}.fromkeys(int_fields, int))
# stats.sort("python_rank")
# stats[:40].sort("timestamp").select("timestamp all_books_rank data_processing_rank python_rank software_development_rank").present()
stats.add_field("date", lambda rec: lt.Table.parse_date("%Y-%m-%d %H:%M:%S")(rec.timestamp))

# pivot to group entries into subtables by date
stats.create_index("date")
piv = stats.pivot("date")

# create table of best Python ranking for each day
best_by_day = lt.Table()
for day_recs in piv.subtables:
    best_by_day.insert(min(day_recs, key=lambda rec: rec.python_rank))
best_by_day.create_index("date")

# first day in top 100 Python books
start_date = date(2023, 4, 7)

# get daily bests where Python rank is <= 100, beginning at start_date
streak_threshold = 500
top_n_streak = lt.Table().insert_many(
    takewhile(
        lambda rec: rec.python_rank <= streak_threshold,
        best_by_day.by.date[start_date:]
    )
)(f"Days in the Top {streak_threshold} Python Books on Amazon")

streak_len = len(list(takewhile(lambda rec: rec.python_rank <= streak_threshold, best_by_day[::-1])))

# present the results, with a summary caption
top_n_streak.select("date python_rank all_books_rank").present(
    caption=f"{streak_len} days in the top {streak_threshold} Python books",
    caption_justify="left",
)

print()
print(f"Highest ranking among Python books: #{min(stats.all.python_rank)}")