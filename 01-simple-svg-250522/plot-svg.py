from pyaxidraw import axidraw
ad = axidraw.AxiDraw()

# Load file and configure plot context
ad.plot_setup("shape-01.svg")

# Adjust plotter settings to match idraw
# Override native res factor to the idraw plotter
ad.params.native_res_factor = 1270.0

# Set measurements to cm
ad.options.units = 1 

# Set pen up and down positions
ad.options.pen_pos_up = 20
ad.options.pen_pos_down = 45

ad.plot_run()
