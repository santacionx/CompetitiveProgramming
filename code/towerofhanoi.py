def tower(d,a,b,c):
    if(d==1):
        print(f"move disk {d} from {a} to {c}")
        return
    tower(d-1,a,c,b)
    print(f"move disk {d} -> {a} to {c}")
    tower(d-1,b,a,c)

tower(10,"start","mid","end")