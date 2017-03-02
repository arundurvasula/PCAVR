

SCALE=15
out = open("pca.html", 'w')
out.write("<!DOCTYPE html>\n")
out.write("<html>\n<head>\n<meta charset='utf-8'>\n<title>PCA</title>\n<script src='https://aframe.io/releases/0.5.0/aframe.min.js'></script>\n</head>\n")
out.write("<body>\n<a-scene>\n")
with open("test.eigenvec", 'r') as eig:
    for line in eig:
        s1,s2,x,y,z = line.split(" ")[0:5]
        x = float(x)
        y = float(y)
        z = float(z)
        out.write("<a-sphere position='"+str(x*SCALE)+ " "+str(y*SCALE)+ " "+str(z*SCALE)+ " "+"' radius='0.15' color='#EF2D5E'></a-sphere>\n")

out.write('<a-sky color="#ECECEC"></a-sky>')
out.write("</a-scene></body></html>")
