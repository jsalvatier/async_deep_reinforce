virtualenv env
source env/bin/activate

brew install opencv
cp /usr/local/Cellar/opencv/2.4.13_3/lib/python2.7/site-packages/* env/lib/python2.7/site-packages/

pip install tensorflow 
pip install gym
pip install git+https://github.com/jsalvatier/PyGame-Learning-Environment 
pip install git+https://github.com/lusob/gym-ple.git

brew install sdl sdl_ttf sdl_image sdl_mixer portmidi


#install ALE
git clone https://github.com/miyosuda/Arcade-Learning-Environment.git ../
cd ../Arcade-Learning-Environment
cmake -DUSE_SDL=ON -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=OFF .
make -j 4
cd ../async_deep_reinforce

pip install ../Arcade-Learning-Environment
