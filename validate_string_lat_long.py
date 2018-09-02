def find_lat_log(arr):
    for co_ordinate in arr:
        first_half = ""
        second_half = ""
        if len(co_ordinate.split(",")) > 1:
            first_half = co_ordinate.split(",")[0]
            second_half = co_ordinate.split(",")[1]
            if co_ordinate.startswith("(") and co_ordinate.endswith(")") and (",") in co_ordinate:
                if not " " in first_half[:2] and not " " in first_half[-2:] and not " " in second_half[-2:] and " " in second_half[:3]:
                    try:
                        if first_half.strip("(").strip("+").startswith("0"):
                            print("invalid")
                            return
                        x = float(first_half.strip("(").strip("+"))
                        if second_half.strip(")").strip("-").strip(" ").startswith("0"):
                            print("invalid")
                            return
                        y = float(second_half.strip(")").strip("-").strip(" "))
                    except:
                        x=y=0
                        pass
                    if x and y and -90 <= x <= 90 and -180 <= y <= 180:
                        print("valid")
                    else:
                        print("invalid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")

if __name__=="__main__":
    arr = ["(90, 110 )", "(90, 180)", "(+90, -120)", "(90, +180)"]
    find_lat_log(arr)
