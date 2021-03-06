from audiovibe.extract.preprocessing import Samples
from audiovibe.extract.features import Features
from audiovibe.think.predict import predict, load_model

if __name__ == "__main__":

    path = "test/Beethoven - Moonlight Sonata (1st Movement)_test.m4a"
    # path = "test/vivaldi_storm.m4a"
    # path = "test/relaxed45_test.m4a"
    samples = Samples.from_path(path)
    features = Features.from_samples(samples)

    model = load_model()
    emotion = predict(model, features)
    print(emotion)
