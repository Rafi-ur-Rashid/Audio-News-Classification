# Audio News Classification

## Models for Experimentation

## Wav2Vec
- Pretrained for Bangla: https://huggingface.co/tanmoyio/wav2vec2-large-xlsr-bengali

### 2D
- ✔️ CNN Model
- ✔️ Transfer Learning using Image SOTA models eg. VGG, ResNet, etc.
- CNN with Attention (Pervasive Attention ... used in Machine Translation, can it be used here ?)
- Image Transformer

### 1D
- Transformer (Encoder + Dense for classification)
- LSTM with Attention
- ✔️ LSTM
- 1D CNN
- C-LSTM

### Miscalenous
- Speech To Text (STT) module (eg. Google's STT module) to retrieve text, then run various text classifiers ?
  - HuggingFace's m-Bert
  - Naive Bag Of Words with classifier

## Different Features to experiment with

- ✔️ MFCC
- Mel Spectrograms
- Discrete Fourier Transform for voice normalization ?
- FFT
- CTF ??


## Different methodologies for future
- Stream/online or real-time classification ?
- BoAP: Bag of audio & phrases descriptor
