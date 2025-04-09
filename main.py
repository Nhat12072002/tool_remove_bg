from background_remove import BackgroundRemover

def main():
    remover = BackgroundRemover()
    if remover.choose_image():
        remover.remove_background()

if __name__ == "__main__":
    main()
