class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6804892450"
    sudo_users = "7613349267", "6804892450"
    GROUP_ID = -1002664732443
    TOKEN = "7681634301:AAGHIDuah7ITs_0TPvt0BdfKxBVIKTsQWC8"
    mongo_url = "mongodb+srv://jowan20678:qGcqHCgAOiYnwG9K@cluster0sddji.3cetple.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0sddji"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "fghu6yt"
    UPDATE_CHAT = "fghu6yt"
    BOT_USERNAME = "Waifubots_bot"
    CHARA_CHANNEL_ID = "-1002362397427"
    api_id = 27479878
    api_hash = "05f8dc8265d4c5df6376dded1d71c0ff"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
