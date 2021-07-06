import argparse
import os
import librosa
import soundfile as sf

parser = argparse.ArgumentParser()
parser.add_argument('--wav-path', type=str)
parser.add_argument('--dest-path', type=str)
parser.add_argument('--input', type=str)
parser.add_argument('--output', type=str)

args = parser.parse_args()


os.makedirs(args.dest_path, exist_ok=True)

f = open(args.input)
data = f.readlines()
f.close()

wf = open(args.output, 'w')
count = len(data)
for line in data:
    items = line.strip().split("\t")
    wav_name = items[0]
    new_wav_name = os.path.join(args.dest_path, wav_name)
    if not os.path.exists(new_wav):
	y, sr = librosa.load(os.path.join(args.wav_path, wav_name), sr=16000)
	sf.write(new_wav_name, y, sr)
	infos = sf.info(new_wav)
	frames = infos.frames
	sr = infos.samplerate
	wf.write("{}\t{}\t{}\n".format(old_wav, frames, sr))
	count += 1
	if count % 100 == 0:
	    print('process {} done'.format(count))

wf.close()
