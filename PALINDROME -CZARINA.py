#PALINDROME
#CZARINA ORTENERO

yna = " A man a plan a caret a rec a manana an anabasis a tsar a tanager an araban a mat an aromatic an amadan a melanoma an anatman an amowt a barege a jar a tav an arr a parataxis an amora an agron an ami a caress a paracasein a salad an allopath a baronet an all a darer a caravan an alg a ratal an alfa an agnate an arg an arcs an arcanum an air an alp a nail a runon an aid a ratan an anabas a pat an ain a baron a manakin a natator a tarok an attar an apa a nag an animator ot a min a nagana a pan a rattan a kor a tarot a tan an ikan a manor a banian a tapas a ban an anat a radian a nonUralian a planarian a mun a cran a scr an agr an aet a ngana a flan a lat a raglan a navar a carer a dallan a tenor a baht a pollan a dal a sanies a car a passer a caiman an organa a roman a six a tar a parr an avatar a jaeger a batwoman an amt an ana a mon a leman a daman a cit a mor an ataman a bar an areg an atar a stasis a banana a nan a macerater a canal Panama "

yna = yna.replace(" ","")
yna = yna.lower()

#convert the string into list
yna_list = list(yna)


#reverse the list
yna_rev = yna_list[::-1]


#conditional statement
if yna_rev == yna_list:
    print ("\n\n\n THE INPUT IS PALINDROME")
else:
    print ("\n\n\n THE INPUT IT IS NOT PALINDROME")

