'''
Our programmer friend Micro just taught his son, Micro Junior, how to read a clock. Few days back he also taught him about palindromes. Now as we know that Micro Junior looks for opportunities to trouble his father, so he started asking him questions. He asked him T questions. In each he gave his father a starting time and an ending time and asked the number of times in between which are palindromes (see sample explanation for more clarity) . Now Micro asked for your help to solve this problem.

Input:
The first line consists of T, the number of questions.
Next T lines consist of a starting time S and an ending time E separated by a space. Time is given in 24-hour format without any colons. (See sample input)

Output:
Print the answer for each question in a new line.

Constraints:
1 ≤ T ≤ 1000
It is assured that every time given is valid. Time starts from 0000 to 2359
S ≤ E



SAMPLE INPUT

3
0100 0200
1100 1300
1331 1441

SAMPLE OUTPUT

1
2
2

Explanation

Between 0100 and 0200, only palindromic time is 0110.
Between 1100 and 1300, palindromic times are 1111 and 1221.
Between 1331 and 1441, palindromic times are 1331 and 1441.

'''

def palindrome(time):
    rev = time[-1::-1]
    if(time==rev):
        return 1
    else:
        return 0    

for _  in range(int(input())):
    start,end = map(str,input().split())
    cnt = 0
    for time in range(int(start),int(end)+1):
        if(time%100<=59):
            time = '{0:04d}'.format(time)
            if(palindrome(time)):
                cnt+=1        
    print(cnt)
