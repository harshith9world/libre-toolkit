if __name__ == "__main__":

    from engine import find_delimiter
    test_text = "Hello!, harshit"
    
    result = find_delimiter(
        text=test_text,
        delimiter="!",
        instance=1,
        case_sensitive=True
        )
    print(f'result : {result} {len(test_text)}' )