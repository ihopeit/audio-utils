# split an audio file to small files which has minimum length as 1 secs, and maximum as 10 secs.
auditok -i ~/input.wav -o output_{N}_{start}_{end}.wav -n 1 -m 10

#plot an audio file:
#auditok -i ~/input.wav -p
