docker run --rm -it \
--gpus all \
-v `pwd`/api:/api \
-v `pwd`/data:/data \
-v `pwd`/scripts:/obj-det \
-p 5699:5699 \
igormcsouza/object-detection:development