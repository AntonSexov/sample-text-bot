from image_processing import add_text_to_image



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Input file and output file need to be in command line arguments")
    else:
        try:
            if sys.argv[3] != None and sys.argv[4] != None:
                add_text_to_image(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
            else:
                add_text_to_image(sys.argv[1], sys.argv[2])
        except IndexError:
            add_text_to_image(sys.argv[1], sys.argv[2])
        







            