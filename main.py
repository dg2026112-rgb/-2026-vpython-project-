#20261103
sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
sphere(size = vec(0.075,0.075,0.075),pos=vec(-0.13,0,0.5),radius=1,color=color.black)
sphere(size = vec(0.075,0.075,0.075),pos=vec(0.13,0,0.5),radius=1,color=color.black)
r=ring(axis=vec(1,1,0.5),pos=vec(0,-0.15,0.5),radius=0.04,color=color.black)


#20261105
sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
sphere(size = vec(0.075,0.075,0.075),pos=vec(-0.13,0,0.5),radius=1,color=color.black)
sphere(size = vec(0.075,0.075,0.075),pos=vec(0.13,0,0.5),radius=1,color=color.black)
r=ring(axis=vec(1,1,0.5),pos=vec(0,-0.15,0.5),radius=0.04,color=color.black)
box(axis=vec(1,1,0.5), size = vec(0.05,0.005,0.01),pos=vec(-0.08,-0.11,0.5),color=color.black)
cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
box(size = vec(0.1,0.01,0.01),pos=vec(0,-0.11,0.5),color=color.black)
box(size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
box(size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.03,-0.11,0.5),color=color.black)
box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.03,-0.11,0.5),color=color.black)
cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))


#20261112
import random
bori_head=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left=sphere(size = vec(0.075,0.075,0.075),pos=vec(-0.13,0,0.5),radius=1,color=color.black)
eye_right=sphere(size = vec(0.075,0.075,0.075),pos=vec(0.13,0,0.5),radius=1,color=color.black)
bori_mouth=r=ring(axis=vec(1,1,0.5),pos=vec(0,-0.15,0.5),radius=0.04,color=color.black)
mouth_left=box(axis=vec(1,1,0.5), size = vec(0.05,0.005,0.01),pos=vec(-0.08,-0.11,0.5),color=color.black)
bori_body=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_biuseum=compound([bori_head,ear_right,ear_left,eye_left,eye_right,bori_mouth,mouth_left,bori_body])

bori_head2=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right2=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left2=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0,-0.11,0.5),color=color.black)
eye_right2=box(size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
mouth_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
bori_body2=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_mupyojeong=compound([bori_head2,ear_right2,ear_left2,eye_left2,eye_right2,bori_mouth2,mouth_left2,bori_body2])



bori_head3=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right3=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left3=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left3=box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
eye_right3=box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
mouth_left3=box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.03,-0.11,0.5),color=color.black)
bori_love3=box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.03,-0.11,0.5),color=color.black)
bori_body3=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_angry=compound([bori_head3,ear_right3,ear_left3,eye_left3,eye_right3,bori_mouth3,mouth_left3,bori_body3,bori_love3])

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :

bori_head=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left=sphere(size = vec(0.075,0.075,0.075),pos=vec(-0.13,0,0.5),radius=1,color=color.black)
eye_right=sphere(size = vec(0.075,0.075,0.075),pos=vec(0.13,0,0.5),radius=1,color=color.black)
bori_mouth=r=ring(axis=vec(1,1,0.5),pos=vec(0,-0.15,0.5),radius=0.04,color=color.black)
mouth_left=box(axis=vec(1,1,0.5), size = vec(0.05,0.005,0.01),pos=vec(-0.08,-0.11,0.5),color=color.black)
bori_body=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_biuseum=compound([bori_head,ear_right,ear_left,eye_left,eye_right,bori_mouth,mouth_left,bori_body])

while True:
    rate(50)
    k=keysdown()
    if 'up' in k:
        bori_biuseum.pos.y+=0.1
    if 'down' in k:
        bori_biuseum.pos.y-=0.1
    if 'left' in k:
        bori_biuseum.pos.x-=0.1
    if 'right' in k:
        bori_biuseum.pos.x+=0.1


bori_head2=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right2=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left2=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0,-0.11,0.5),color=color.black)
eye_right2=box(size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
mouth_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
bori_body2=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_mupyojeong=compound([bori_head2,ear_right2,ear_left2,eye_lef2t,eye_right2,bori_mouth2,mouth_left2,bori_body2])

while True:
    rate(50)
    k=keysdown()
    if 'up' in k:
        bori_mupyojeong.pos.y+=0.1
    if 'down' in k:
        bori_mupyojeong.pos.y-=0.1
    if 'left' in k:
        bori_mupyojeong.pos.x-=0.1
    if 'right' in k:
        bori_mupyojeong.pos.x+=0.1


sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.03,-0.11,0.5),color=color.black)
box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.03,-0.11,0.5),color=color.black)
cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :

















bori_head2=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right2=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left2=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0,-0.11,0.5),color=color.black)
eye_right2=box(size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
mouth_left2=box(size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
bori_body2=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_mupyojeong=compound([bori_head2,ear_right2,ear_left2,eye_lef2t,eye_right2,bori_mouth2,mouth_left2,bori_body2])



bori_head3=sphere(size = vec(1,1,1),pos=vec(0,0,0),radius=1,color=vec(255/255,246/255,231/255))
ear_right3=sphere(size = vec(0.3,0.65,0.3),pos=vec(0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,0.5,0))
ear_left3=sphere(size = vec(0.3,0.65,0.3),pos=vec(-0.5,0.05,0.15),radius=1,color=vec(185/255,122/255,86/255),axis=vec(1.5,-0.5,0))
eye_left3=box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.13,0,0.5),color=color.black)
eye_right3=box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.13,0,0.5),color=color.black)
mouth_left3=box(axis=vec(1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(-0.03,-0.11,0.5),color=color.black)
bori_love3=box(axis=vec(-1,1,0.5),size = vec(0.1,0.01,0.01),pos=vec(0.03,-0.11,0.5),color=color.black)
bori_body3=cone(pos=vec(0, -0.8, 0), axis=vec(0, 1, 0), radius=0.5, color=vec(255/255,246/255,231/255))

bori_angry=compound([bori_head3,ear_right3,ear_left3,eye_left3,eye_right3,bori_mouth3,mouth_left3,bori_body3,bori_love3])

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :

