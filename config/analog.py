## _lights [(label, wavelength, dsp line, sim diffraction angle at slm),...]
aout_keys = ['name', 
             'cockpit_axis', 
             'line', 
             'sensitivity', 
             'hard_limits', 
             'soft_limits', 
             'deltas', 
             'default_delta']

aouts = [(
            'polrot',   # polarisation rotatoar
            'SI angle',    # moves angle 
            2,          # on analogue out 2
            1,          # 1V per V
            (0, 10),
            (None, None),
            [0.01, 0.05, 0.1, 0.5, 1],
            2
         ),
         (
            'z_insert',
            'z',
            0,
            20,         # microns / V
            (0, 200),
            (None, None),
            [.05, .1, .5, 1],
            2,
         )  
        ]
