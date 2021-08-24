def triangle_area (b,h):
    answer = (b*h)/2
    return answer

if __name__ == "__main__":
    base = 10
    height = 15
    area = triangle_area(base,height)
    print(f"The trianger area with base={base} and height={height} is {area}.")