import sys
import mock


def test_setup():
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi.GPIO'] = mock.Mock()
    sys.modules['smbus'] = mock.Mock()
    import trackball
    device = trackball.TrackBall()
    del device
