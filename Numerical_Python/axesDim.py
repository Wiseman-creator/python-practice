import numpy as np

arr1D = np.array([1, 2, 3])

arr2D = np.array([[1, 2, 3], [4, 5, 6]])

arr3D = np.array(
    [
        [[1, 2, 9], [3, 4, 9], [1, 1, 1]],
        [[4, 5, 9], [5, 6, 9], [1, 1, 1]],
        [[6, 7, 9], [7, 8, 9], [1, 1, 1]],
    ]
)

arr4D = np.arange(1, 121).reshape(2, 3, 4, 5)

marks = np.array([[80, 75, 90], [70, 85, 95], [60, 88, 78]])

total_marks = np.sum(marks, axis=0)
total_stud_marks = np.sum(marks, axis=1)
print(total_marks,total_stud_marks)