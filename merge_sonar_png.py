from PIL import Image

def merge_sonar_png(port_path, star_path, output_path): 
    #Loading images 
    port = Image.open(port_path).convert("RGB")
    star = Image.open(star_path).convert("RGB")

    #Match heights with padding 
    height = max(port.height, star.height)

    def pad(img): 
        if img.height == height: 
            return img
        padded = Image.new("RGB", (img.width, height), (0, 0, 0))
        padded.paste(img, (0, 0))
        return padded
    
    port = pad(port) 
    star = pad(star)

    #Create blank canvas merging
    mosaic = Image.new("RGB", (port.width + star.width, height)); 

    #Pasting images side by side on blank canvas (port left, star right)
    mosaic.paste(port, (0, 0))
    mosaic.paste(star, (port.width, 0))

    mosaic.save(output_path)
    print("Merged sonar mosaic produced, and saved to:", output_path)