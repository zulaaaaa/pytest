import requests 

print("MMMMMMMMMMW0d:'.        .':d0WMMMMMMMMMM")
print("MMMMMMMMWO:.                .:OWMMMMMMMM")
print("MMMMMMMNo.                    .dNMMMMMMM")
print("MMMMMMMNo.                    .dNMMMMMMM")
print("MMMMMMMk.                      .kMMMMMMM")
print("MMMMMMWo                        oWMMMMMM")
print("MMMMMMMx.                      .xMMMMMMM")
print("MMMMMMM0,   ....        ....   ,KMMMMMMM")
print("MMMMMMMWo.'dKXNKl.    .lKXXKd..dWMMMMMMM")
print("MMWWMMMWo.lWMMMNd.    .dNMMMNl.oWMMWWWMM")
print("Ko;,lKWx. .colc,. ,ll, .,cloc. .xWKl,;oK")
print("d.   lNO'        ,0MMO'        ,0Nc   .x")
print(":    .;c:,.. .   :kkkk;   . .',:c,.   .c")
print(".  ';'.   . .l;          :l. .   .,;'  .")
print("OdkXWN0xc'.  cd,........,dc  .'cx0NWXkxO")
print("MMMMMMMMMN0l..;cccc::cccc,..l0NMMMMMMMMM")
print("MMMMMMMMWXOc.   ........   .lOXWMMMMMMMM")
print("koxXWXOd:.                    .:dONWKxok")
print(".  .,.   .';lxko;......;okdl;..   ',.  .")
print("c.   .:ok0NWMMMMWXXXXXXWMMMMWN0ko:.   .c")
print("d.   oWMMMMMMMMMMMMMMMMMMMMMMMMMMNl   .x")
print("0,  'OMMMMMMMMMMMMMMMMMMMMMMMMMMMMO'  ;0")
print("                                        ")
print("________________________________________")
print("             made by zulaa              ")
print("              Version 1.0               ")
print("Git : https://github.com/zulaaaaa/pytest")
print("________________________________________")
print("                                        ")

target = str(input("pls enter domain : example : https://google.com/"))
counter = 1 

print("good request means that the request came throu")
running = False
x = requests.get(target).status_code
test = int(input("pls insert int 1 to start "))
if test == 1 : 
    running = True
    while running is True:
        counter = counter + 1  
        requests.get(target)
        if x == 200 :
            print(f"http_request{counter} good request ")
        else :
            running = False 
            print("bad request program end ")
            quit()
    else :
        print("fail")
else : 
    print("you cose not to start ")