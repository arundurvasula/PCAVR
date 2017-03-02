

SCALE=15
out = open("pca.html", 'w')
out.write("<!DOCTYPE html>\n")
out.write("<html>\n<head>\n<meta charset='utf-8'>\n<title>PCA</title>\n<script src='https://aframe.io/releases/0.5.0/aframe.min.js'></script>\n</head>\n")
out.write("<body>\n<a-scene>\n")
out.write("""
<a-camera look-controls wasd-controls fly='true'></a-camera>
""")
#out.write("""
#<a-entity camera><a-entity cursor='fuse: true; fuseTimeout: 500' #position='0 0 -1' geometry='primitive: ring; radiusInner: 0.02; #radiusOuter: 0.03' material='color: black; shader: flat'></a-entity></#a-entity>""")
with open("test.eigenvec", 'r') as eig:
    for line in eig:
        s1,s2,s3,x,y,z = line.split(" ")[0:6]
        x = float(x)
        y = float(y)
        z = float(z)
        out.write("<a-sphere position='"+str(x*SCALE)+ " "+str(y*SCALE)+ " "+str(z*SCALE)+ " "+"' radius='0.15' color='"+s1+"' text='value: "+s2+"; color: white'></a-sphere>\n")

out.write('<a-sky color="#2F4F4F"></a-sky>')
out.write("</a-scene></body></html>")
