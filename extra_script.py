import os

Import("env")

env.BuildSources(
    os.path.join("$BUILD_DIR", ".pio","libdeps","esp32-s3-Sunton_800x480","lvgl", "build"),
    os.path.join("$PROJECT_DIR", ".pio","libdeps","esp32-s3-Sunton_800x480","lvgl","demos")
)
