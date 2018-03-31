nameofstudents = ['yna','aubrey','chow','shiela','yna','shiela','shiela','aubrey',
                'chow','chow','klienth','yna','paolo','jade','jade','athena'
                'czarina','madel','shiela','aubrey','aubrey','shiela','shiela',
                'klienth','chow','paolo','klienth','chow','mau','yna','mark',
                'jade','yna','aubrey','christian','shiela','juan','ana','yna',
                'yna','sheila','christian','shiela','juan','yna','athena','mae'
                'aubrey','yna','mark','ana','yna','christian',',mae','czedrick'
                'chow','paul','aubrey','madel','shiela','juan','madel','czarina'
                'cedrick','yna','ana','christian','shiela','paolo','aubrey','ela']


from collections import Counter
nameofstudents_counts = Counter(nameofstudents)
top_five = nameofstudents_counts.most_common(5)
print "LIST OF TOP 5 SURVIVING STUDENTS :) "
print(top_five)
