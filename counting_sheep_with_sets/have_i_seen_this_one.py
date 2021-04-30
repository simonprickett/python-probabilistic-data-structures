sheep_seen = { 
    "1934", "1201", "1199", "0007", "3409", "1015"
}

def have_i_seen(sheep_id):
    if sheep_id in sheep_seen:
        print(f"I have seen sheep {sheep_id}.")
    else:
        print(f"I have not seen sheep {sheep_id}.")

have_i_seen("1934")
have_i_seen("1283")