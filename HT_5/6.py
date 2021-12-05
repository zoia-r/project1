"""
6. �� �� ����� ���� ������� �� <range>. �������� ���� ��������� ���� �������.
   P.S. ������� ��������� ���������.
   P.P.S. ��� ������� �������� ���� ������� - ����� �������� ������������ �� ���:
   https://docs.python.org/3/library/stdtypes.html#range
  
"""


def range_new(start, finish=0, step=1):
    if finish == 0:
        finish = start
        start = 0
    if step ==0:
        raise ValueError()
    if step>0:
        while start < finish:
            yield start
            start += step
    else:
        while start > finish:
            yield start
            start += step



for i in range_new(2):
    print(i)


for i in range_new(1, 10):
    print(i)


for i in range_new(10, 1, -2):
    print(i)
