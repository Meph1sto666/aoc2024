from warden import Warden, find_warden

w: Warden = find_warden([[c for c in l] for l in open("./0601.txt")])
print(len(set(w.patrol())))