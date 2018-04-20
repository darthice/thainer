from tltk import nlp
import tltk
import codecs


def run(sen):
    test=sen#ประโยคที่ใช้ทดสอบ
    test=tltk.nlp.word_segment(test)#ตัดคำ
    test=test.replace("<s/>","")#เอา</s>ออกจากประโยค
    #print(test)
    sentolist(test)


#ทำให้ประโยคจากการตัดคำกลายเป็นlist
def sentolist(test):
    stat=0
    end=0
    test_it=[]
    for i in range(len(test)):
        if test[i] == "|":
            end=i
            test_it.append(test[stat:end])
            stat=i+1
    test_it.append(test[stat:len(test)])
    ngram(test_it)

#เริ่มทำ n-gram
def ngram(test_it):
    #นำคำจาก custom_token มาใส่ใน token
    with codecs.open('custom_token.txt', 'r', "utf-8") as f:
        lines = f.readlines()
    token=[e.strip() for e in lines]
    del lines
    f.close() # ปิดไฟล์
    for i in range(len(test_it)-1):#ลูปตามขนาดของจำนวนคำ-1 เพราะในรอบสุดท้ายมันไม่มีคำต่อแล้ว
        word=""
        #print(i)
        for j in range(len(test_it)-i-1):#ลูปตามอักษรที่เหลือ-1 เพราะเราไม่เอาตัวสุดท้าย    
            if j==0:#ถ้า word ไม่มีค่าใดให้ใส่คำจาก test_it[i] ลงไป(คำแรก)
                word=test_it[i]
            else:#ถ้ามีอยู่แล้วเอาคำตำแหน่งถัดไปมาต่อเพิ่ม
                word=word+test_it[i+j]

            #print(word)
            if word in token:#ถ้าคำนี้อยู่ในพจนานุกรมของเรา
                test_it[i]=word#เอาคำนี้ไปแทนที่คำเก่าใน test_it
                for x in range(i+1,i+j+1):#แทนที่คำที่นำมาต่อด้วย <>
                    #print(x)
                    test_it[x]="<>"
                
     #ลบ <> ออกจาก list               
    position=[]
    for i in range(len(test_it)):#ลบ <> ออกจาก list
        if test_it[i]=="<>":
            position.append(i)
    position.reverse()
    for i in position:
        del test_it[i]
    test_it.pop()

    print(test_it)
