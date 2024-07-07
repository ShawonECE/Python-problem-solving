def flipAndInvertImage(image):
    n = len(image[0])
    for i in range(n):
        left = 0
        right = n - 1
        while left <= right:
            if left == right:
                if image[i][left] == 0:
                    image[i][left] = 1
                else:
                    image[i][left] = 0
            else:
                if image[i][left] != image[i][right]:
                    image[i][left], image[i][right] = image[i][right], image[i][left]
                
                if image[i][left] == 0:
                    image[i][left] = 1
                else:
                    image[i][left] = 0
                    
                if image[i][right] == 0:
                    image[i][right] = 1
                else:
                    image[i][right] = 0
                
            left+=1
            right-=1
    
    return image

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(image))