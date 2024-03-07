def count_item_and_sort(items):
    # Menghitung jumlah kemunculan setiap item
    item_count = {}
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    # Mengurutkan item berdasarkan abjad
    sorted_items = sorted(set(item_count[item]))

    # Menghasilkan string hasil perhitungan
    result = ""
    for item in sorted_items:
        result += f"{item}->{item_count.get(item, 0)} "

    return result.strip()



if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"