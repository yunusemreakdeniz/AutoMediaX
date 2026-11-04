#!/usr/bin/env python3
"""Non-invasive source checks for the UI/performance-only change set."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
controller = (root / 'fermata/src/main/java/me/aap/fermata/ui/view/PhonePlaybackCarHeaderController.java').read_text()
layout = (root / 'fermata/src/main/res/layout/phone_open_on_car_strip.xml').read_text()
assert 'header.removeCallbacks(pendingRender);' in controller
assert 'if (closed) return;' in controller
for button in ('phone_header_previous', 'phone_header_play_pause', 'phone_header_next'):
    assert '@+id/' + button in layout
assert 'android:layout_width="56dp"' in layout
assert (root / 'fermata/src/main/java/me/aap/fermata/ui/activity/VoiceRecognitionSession.java').exists()
assert (root / 'fermata/src/main/java/me/aap/fermata/ui/activity/SpeechRecognitionSupport.java').exists()
print('UI/performance scope checks passed; voice sources retained.')
