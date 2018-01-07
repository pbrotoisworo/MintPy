from Tkinter import *

import h5py
import matplotlib
matplotlib.use('TkAgg')
import tkFileDialog as filedialog
import view as view
import info
import _readfile as readfile

def pick_file():
    global attributes

    if h5_file.get() == "":
        filename = filedialog.askopenfilename(initialdir="/User/Joshua/", title="Select file",
                                              filetypes=(("jpeg files", "*.h5"), ("all files", "*.*")))
        frame.filename = filename
        h5_file.set(frame.filename)
        h5_file_short.set(filename.split("/")[-1])
        pick_h5_file_button.config(text="Cancel")

        attributes = readfile.read_attribute(h5_file.get())

        set_variables_from_attributes()

        return frame.filename
    else:
        h5_file.set("")
        h5_file_short.set("No File Selected")
        pick_h5_file_button.config(text="Select .h5 File")


def pick_mask():
    if mask_file.get() == "":
        filename = filedialog.askopenfilename(initialdir="/User/Joshua/", title="Select file",
                                              filetypes=(("jpeg files", "*.h5"), ("all files", "*.*")))
        frame.filename = filename
        mask_file.set(frame.filename)
        mask_short.set(filename.split("/")[-1])
        pick_mask_file_button.config(text="Cancel")
        return frame.filename
    else:
        mask_file.set("")
        mask_short.set("No File Selected")
        pick_mask_file_button.config(text="Select Mask File")


def pick_dem():
    if dem_file.get() == "":
        filename = filedialog.askopenfilename(initialdir="/User/Joshua/", title="Select file",
                                              filetypes=(("jpeg files", "*.h5"), ("all files", "*.*")))
        frame.filename = filename
        dem_file.set(frame.filename)
        dem_short.set(filename.split("/")[-1])
        pick_dem_file_button.config(text="Cancel")
        return frame.filename
    else:
        dem_file.set("")
        dem_short.set("No File Selected")
        pick_dem_file_button.config(text="Select Topography File")


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


def show_file_info(file_info):

    window = Tk()
    window.minsize(width=350, height=550)
    window.maxsize( height=550)
    window.resizable(width=True, height=False)

    text_box = Text(window, wrap=NONE)
    text_box.insert(END, file_info)
    text_box.config(height=550)
    text_box.config(state=DISABLED)

    text_box.pack(fill=X)

def show_plot():

    print(scalebar_distance.get())
    print(scalebar_lat.get())
    print(scalebar_lon.get())

    options = [h5_file.get(), "-m", str(y_lim_lower.get()), "-M", str(y_lim_upper.get()), "--alpha", str(transparency.get()), "--figext",
    fig_ext.get(), "--fignum", fig_num.get(), "--coord", coords.get()]

    if mask_file.get() != "":
        options.append("--mask")
        options.append(mask_file.get())

    if unit.get() != "":
        options.append("-u")
        options.append(unit.get())
    if colormap.get() != "":
        options.append("-c")
        options.append(colormap.get())
    if projection.get() != "":
        options.append("--projection")
        options.append(projection.get())
    if lr_flip.get() == 1:
        options.append("--flip-lr")
    if ud_flip.get() == 1:
        options.append("--flip-ud")
    if wrap.get() == 1:
        options.append("--wrap")
    if opposite.get() == 1:
        options.append("--opposite")

    if dem_file.get() != "":
        options.append("--dem")
        options.append(dem_file.get())
    if shading.get() == 0:
        options.append("--dem-noshade")
    if countours.get() == 0:
        options.append("--dem-nocontour")
    if countour_smoothing.get() != "":
        options.append("--contour-smooth")
        options.append(countour_smoothing.get())
    if countour_step.get() != "":
        options.append("--contour-step")
        options.append(countour_step.get())

    if subset_x_from.get() != "" and subset_x_to.get() != "":
        options.append("-x")
        options.append(subset_x_from.get())
        options.append(subset_x_to.get())
    if subset_y_from.get() != "" and subset_y_to.get() != "":
        options.append("-y")
        options.append(subset_y_from.get())
        options.append(subset_y_to.get())
    if subset_lat_from.get() != "" and subset_lat_to.get() != "":
        options.append("-l")
        options.append(subset_lat_from.get())
        options.append(subset_lat_to.get())
    if subset_lon_from.get() != "" and subset_lon_to.get() != "":
        options.append("-L")
        options.append(subset_lon_from.get())
        options.append(subset_lon_to.get())

    if ref_x.get() != "" and ref_y.get() != "":
        options.append("--ref-yx")
        options.append(ref_y.get())
        options.append(ref_x.get())
    if ref_lat.get() != "" and ref_lon.get() != "":
        options.append("--ref-lalo")
        options.append(ref_lat.get())
        options.append(ref_lon.get())
    if show_ref == 0:
        options.append("--noreference")
    if ref_color.get() != "":
        options.append("--ref-color")
        options.append(ref_color.get())
    if ref_sym.get() != "":
        options.append("--ref-symbol")
        options.append(ref_sym.get())

    ''' "--ref-color", ref_color.get(), "--ref-symbol", ref_sym.get() '''

    if font_size.get() != "":
        options.append("-s")
        options.append(font_size.get())
    if plot_dpi.get() != "":
        options.append("--dpi")
        options.append(plot_dpi.get())
    if row_num.get() != "":
        options.append("--row")
        options.append(row_num.get())
    if col_num.get() != "":
        options.append("--col")
        options.append(col_num.get())
    if axis_show.get() == 0:
        options.append("--noaxis")
    if tick_show.get() == 0:
        options.append("--notick")
    if title_show.get() == 0:
        options.append("--notitle")
    if cbar_show.get() == 0:
        options.append("--nocbar")
    if title_in.get() == 1:
        options.append("--title-in")
    if title.get() != "":
        options.append("--figtitle")
        options.append(title.get())
    if fig_size_width.get() != "" and fig_size_height.get() != "":
        options.append("--figsize")
        options.append(fig_size_height.get())
        options.append(fig_size_width.get())
    if fig_w_space.get() != "":
        options.append("--wspace")
        options.append(fig_w_space.get())
    if fig_h_space.get() != "":
        options.append("--hspace")
        options.append(fig_h_space.get())

    if coastline.get() != 0:
        options.append("--coastline")
    if resolution.get() != "":
        options.append("--resolution")
        options.append(resolution.get())
    if lalo_label.get() != 0:
        options.append("--lalo-label")
    if lalo_step.get() != "":
        options.append("--lalo-step")
        options.append(lalo_step.get())
    if scalebar_distance.get() != "" and scalebar_lat.get() != "" and scalebar_lon.get() != "":
        options.append("--scalebar")
        options.append(scalebar_distance.get())
        options.append(scalebar_lat.get())
        options.append(scalebar_lon.get())
    if show_scalebar.get() == 0:
        options.append("--noscalebar")

    if save.get() != 0:
        options.append("--save")
    if output_file.get() != "":
        options.append("-o")

        location_parts = h5_file.get().split("/")
        location = "/".join(location_parts[1:-1])

        options.append("/"+str(location)+"/"+output_file.get())

    if show_info.get() == 1:
        file_info = info.hdf5_structure_string(h5_file.get())
        show_file_info(file_info)

    view.main(options)


def set_variables_from_attributes():
    print("")
    subset_x_from.set(attributes['XMIN'])
    subset_y_from.set(attributes['YMIN'])
    subset_x_to.set(attributes['XMAX'])
    subset_y_to.set(attributes['YMAX'])

    set_susbset_lalo_info()


def compute_lalo_subset():
    width = int(float(attributes['WIDTH']))
    length = int(float(attributes['FILE_LENGTH']))
    data_box = (0, 0, width, length)

    lat_step = float(attributes['X_STEP'])
    lon_step = float(attributes['Y_STEP'])
    ul_lon = float(attributes['X_FIRST']) + data_box[0]*lon_step
    ul_lat = float(attributes['Y_FIRST']) + data_box[1]*lat_step
    lr_lon = ul_lon - lon_step * (data_box[2] - data_box[0])
    lr_lat = ul_lat - lat_step * (data_box[3] - data_box[1])

    return ul_lat, ul_lon, lr_lon, lr_lat


def set_susbset_lalo_info():
    ul_lat, ul_lon, lr_lon, lr_lat = compute_lalo_subset()

    subset_lat_from.set(str(round(ul_lat, 2)))
    subset_lon_from.set(str(round(ul_lon, 2)))
    subset_lat_to.set(str(round(lr_lat, 2)))
    subset_lon_to.set(str(round(lr_lon, 2)))

root = Tk()
root.minsize(width=365, height=750)
root.maxsize(width=365, height=750)
root.resizable(width=False, height=False)

submit_button = Button(root, text="Show Plot", command=lambda: show_plot())
submit_button.pack(side=TOP, pady=(10, 20))

canvas = Canvas(root, width=345, height=680)
canvas.pack(side=LEFT, anchor='nw')

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', on_configure)

frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')


colormaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2',
             'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r',
             'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r',
             'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r',
             'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r',
             'Vega20', 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr',
             'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr',
             'bwr_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth',
             'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r',
             'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r',
             'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r',
             'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral', 'spectral_r', 'spring', 'spring_r', 'summer',
             'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r',
             'winter', 'winter_r']

projections = ["cea", "mbtfpq", "aeqd", "sinu", "poly", "moerc", "gnom", "moll", "lcc", "tmerc", "nplaea", "gall",
               "npaeqd", "mill", "merc", "stere", "eqdc", "rotpole", "cyl", "npstere", "spstere", "hammer", "geos",
               "nsper", "eck4", "aea", "kav7", "spaeqd", "ortho", "class", "vandg", "laea", "splaea", "robin"]

attributes = []

'''     Frames, Text Variables, and Widgets for selection of the timeseries.h5 file to plot data from.     '''
pick_h5_file_frame = Frame(frame)

h5_file = StringVar()
h5_file_short = StringVar()
h5_file_short.set("No File Selected")

pick_h5_file_button = Button(pick_h5_file_frame, text='Select Timeseries File', anchor='w', width=15, command=lambda: pick_file())
selected_ts_file_label = Label(pick_h5_file_frame, textvariable=h5_file_short)


'''     Frames, Text Variables, and Widgets for selection of the mask.h5 file to add a mask to the ata.     '''
pick_mask_file_frame = Frame(frame)

mask_file = StringVar()
mask_short = StringVar()
mask_short.set("No File Selected")

pick_mask_file_button = Button(pick_mask_file_frame, text='Select Mask File', anchor='w', width=15, command=lambda: pick_mask())
selected_mask_file_label = Label(pick_mask_file_frame, textvariable=mask_short)





display_options_label = Label(frame, text="DISPLAY OPTIONS:", anchor=W)

'''     Frames, Text Variables, and Widgets for setting y-lim      '''
y_lim_frame = Frame(frame)
y_lim_upper_frame = Frame(y_lim_frame)

y_lim_upper = DoubleVar()
y_lim_upper.set(20)

y_lim_upper_label = Label(y_lim_upper_frame, text="Maximum", width=8)
y_lim_upper_slider = Scale(y_lim_upper_frame, from_=0, to=5000, orient=HORIZONTAL, length=150, variable=y_lim_upper, showvalue=0)
y_lim_upper_entry = Entry(y_lim_upper_frame, textvariable=y_lim_upper, width=6)

y_lim_lower_frame = Frame(y_lim_frame)

y_lim_lower = DoubleVar()
y_lim_lower.set(-20)

y_lim_lower_label = Label(y_lim_lower_frame, text="Minimum", width=8)
y_lim_lower_slider = Scale(y_lim_lower_frame, from_=0, to=5000, orient=HORIZONTAL, length=150, variable=y_lim_lower, showvalue=0)
y_lim_lower_entry = Entry(y_lim_lower_frame, textvariable=y_lim_lower, width=6)

'''     Frames, Text Variables, and Widgets for setting extraneous properties      '''
unit_cmap_projection_frame = Frame(frame)

unit = StringVar()
unit.set("m")
unit_option_menu = apply(OptionMenu, (unit_cmap_projection_frame, unit) + tuple(["cm", "m", "dm", "km", "", "cm/yr", "m/yr", "dm/yr", "km/yr"]))
unit_option_menu.config(width=6)

colormap = StringVar()
colormap_option_menu = apply(OptionMenu, (unit_cmap_projection_frame, colormap) + tuple(colormaps))
colormap_option_menu.config(width=10)
colormap.set('hsv')

projection = StringVar()
projection_option_menu = apply(OptionMenu, (unit_cmap_projection_frame, projection) + tuple(projections))
projection_option_menu.config(width=12)
projection.set("cea")

flip_frame = Frame(frame)

lr_flip = IntVar()
lr_flip_checkbutton = Checkbutton(flip_frame, text="Flip LR", variable=lr_flip)

ud_flip = IntVar()
ud_flip_checkbutton = Checkbutton(flip_frame, text="Flip UD", variable=ud_flip)

wrap = IntVar()
wrap_checkbutton = Checkbutton(flip_frame, text="Wrap", variable=wrap)

opposite = IntVar()
opposite_checkbutton = Checkbutton(flip_frame, text="Opposite", variable=opposite)

transparency = IntVar()
transparency.set(1.0)
transparency_frame = Frame(frame)
transparency_label = Label(transparency_frame, text="Alpha", width=8)
transparency_slider = Scale(transparency_frame, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, length=150, variable=transparency, showvalue=0)
transparency_entry = Entry(transparency_frame, textvariable=transparency, width=6)

show_info = IntVar()
show_info_checkbutton = Checkbutton(frame, text="Show File Info", variable=show_info)



dem_options_label = Label(frame, text="DEM OPTIONS:", anchor=W)

'''     Frames, Text Variables, and Widgets for selection of the topography dem.h5 file to add topography to the data.     '''
pick_dem_file_frame = Frame(frame)

dem_file = StringVar()
dem_short = StringVar()
dem_short.set("No File Selected")

pick_dem_file_button = Button(pick_dem_file_frame, text='Select Topography File', anchor='w', width=15, command=lambda: pick_dem())
selected_dem_file_label = Label(pick_dem_file_frame, textvariable=dem_short)

dem_options_frame = Frame(frame)

shading = IntVar()
shading.set(1)
dem_shading_checkbutton = Checkbutton(dem_options_frame, text="Show Shaded Relief", variable=shading)

countours = IntVar()
countours.set(1)
dem_countours_checkbutton = Checkbutton(dem_options_frame, text="Show Countour Lines", variable=countours)

dem_countour_options = Frame(frame)

dem_countour_smoothing_frame = Frame(dem_countour_options, width=15)

countour_smoothing = StringVar()
countour_smoothing.set("3.0")
dem_countour_smoothing_label = Label(dem_countour_smoothing_frame, text="Contour Smoothing: ", anchor='c', width=15)
dem_countour_smoothing_entry = Entry(dem_countour_smoothing_frame, textvariable=countour_smoothing, width=6)

dem_countour_step_frame = Frame(dem_countour_options, width=15)

countour_step = StringVar()
countour_step.set("200")
dem_countour_step_label = Label(dem_countour_step_frame, text="Countour Step: ", anchor='c', width=15)
dem_countour_step_entry = Entry(dem_countour_step_frame, textvariable=countour_step, width=6)





subset_label = Label(frame, text="SUBSET DATA", anchor=W)

subset_x_frame = Frame(frame)

subset_x_from = StringVar()
subset_x_from_label = Label(subset_x_frame, text="X         From: ")
subset_x_from_entry = Entry(subset_x_frame, textvariable=subset_x_from, width=6)

subset_x_to = StringVar()
subset_x_to_label = Label(subset_x_frame, text="To: ")
subset_x_to_entry = Entry(subset_x_frame, textvariable=subset_x_to, width=6)

subset_y_frame = Frame(frame)

subset_y_from = StringVar()
subset_y_from_label = Label(subset_y_frame, text="Y         From: ")
subset_y_from_entry = Entry(subset_y_frame, textvariable=subset_y_from, width=6)

subset_y_to = StringVar()
subset_y_to_label = Label(subset_y_frame, text="To: ")
subset_y_to_entry = Entry(subset_y_frame, textvariable=subset_y_to, width=6)

subset_lat_frame = Frame(frame)

subset_lat_from = StringVar()
subset_lat_from_label = Label(subset_lat_frame, text="Lat      From: ")
subset_lat_from_entry = Entry(subset_lat_frame, textvariable=subset_lat_from, width=6)

subset_lat_to = StringVar()
subset_lat_to_label = Label(subset_lat_frame, text="To: ")
subset_lat_to_entry = Entry(subset_lat_frame, textvariable=subset_lat_to, width=6)

subset_lon_frame = Frame(frame)

subset_lon_from = StringVar()
subset_lon_from_label = Label(subset_lon_frame, text="Lon      From: ")
subset_lon_from_entry = Entry(subset_lon_frame, textvariable=subset_lon_from, width=6)

subset_lon_to = StringVar()
subset_lon_to_label = Label(subset_lon_frame, text="To: ")
subset_lon_to_entry = Entry(subset_lon_frame, textvariable=subset_lon_to, width=6)





reference_label = Label(frame, text="REFERENCE:", anchor=W)

ref_xy_frame = Frame(frame)

ref_x = StringVar()
ref_x_label = Label(ref_xy_frame, text="X:    ")
ref_x_entry = Entry(ref_xy_frame, textvariable=ref_x, width=6)

ref_y = StringVar()
ref_y_label = Label(ref_xy_frame, text="Y:    ")
ref_y_entry = Entry(ref_xy_frame, textvariable=ref_y, width=6)

ref_latlon_frame = Frame(frame)

ref_lat = StringVar()
ref_lat_label = Label(ref_latlon_frame, text="Lat: ")
ref_lat_entry = Entry(ref_latlon_frame, textvariable=ref_lat, width=6)

ref_lon = StringVar()
ref_lon_label = Label(ref_latlon_frame, text="Lon: ")
ref_lon_entry = Entry(ref_latlon_frame, textvariable=ref_lon, width=6)

show_ref_frame = Frame(frame)

show_ref = IntVar()
show_ref.set(1)
show_ref_checkbutton = Checkbutton(show_ref_frame, text="Show Reference", variable=show_ref)

reference_options_frame = Frame(frame)

ref_color = StringVar()
ref_color_option_menu = apply(OptionMenu, (reference_options_frame, ref_color) + tuple(["b", "g", "r", "m", "c", "y", "k", "w"]))
ref_color_option_menu.config(width=10)
ref_color.set("b")

ref_sym = StringVar()
ref_symbol_option_menu = apply(OptionMenu, (reference_options_frame, ref_sym) + tuple([".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "d", "D", "|", "_"]))
ref_symbol_option_menu.config(width=10)
ref_sym.set(".")

ref_date = StringVar()
ref_date_option_menu = apply(OptionMenu, (reference_options_frame, ref_date) + tuple(["1", "2", "3", "4", "5"]))
ref_date_option_menu.config(width=10)





figure_label = Label(frame, text="FIGURE:", anchor=W)

font_dpi_frame = Frame(frame)

font_size = StringVar()
font_size_label = Label(font_dpi_frame, text="Font Size:    ")
font_size_entry = Entry(font_dpi_frame, textvariable=font_size, width=6)

plot_dpi = StringVar()
dpi_label = Label(font_dpi_frame, text="DPI:    ")
dpi_entry = Entry(font_dpi_frame, textvariable=plot_dpi, width=6)

row_col_num_frame = Frame(frame)

row_num = StringVar()
row_num_label = Label(row_col_num_frame, text="Row Num:   ")
row_num_entry = Entry(row_col_num_frame, textvariable=row_num, width=6)

col_num = StringVar()
col_num_label = Label(row_col_num_frame, text="Col Num:   ")
col_num_entry = Entry(row_col_num_frame, textvariable=col_num, width=6)

axis_cbar_frame = Frame(frame)

axis_show = IntVar()
axis_show.set(1)
axis_show_checkbutton = Checkbutton(axis_cbar_frame, text="Show Axis", variable=axis_show)

cbar_show = IntVar()
cbar_show.set(1)
cbar_show_checkbutton = Checkbutton(axis_cbar_frame, text="Show Colorbar", variable=cbar_show)

title_show = IntVar()
title_show.set(1)
title_show_checkbutton = Checkbutton(axis_cbar_frame, text="Show Title", variable=title_show)

title_tick_frame = Frame(frame)

tick_show = IntVar()
tick_show.set(1)
tick_show_checkbutton = Checkbutton(title_tick_frame, text="Show Ticks", variable=tick_show)

title_in = IntVar()
title_in.set(1)
title_in_checkbutton = Checkbutton(title_tick_frame, text="Title in Axes", variable=title_in)

title_input_frame = Frame(frame)

title = StringVar()
title_input_label = Label(title_input_frame, text="Figure Title: ")
title_input_entry = Entry(title_input_frame, textvariable=title, width=25)

fig_size_frame = Frame(frame)

fig_size_label = Label(fig_size_frame, text="Fig Size")

fig_size_width = StringVar()
fig_size_width_label = Label(fig_size_frame, text="Width: ")
fig_size_width_entry = Entry(fig_size_frame, textvariable=fig_size_width, width=6)

fig_size_height = StringVar()
fig_size_height_label = Label(fig_size_frame, text="Length: ")
fig_size_height_entry = Entry(fig_size_frame, textvariable=fig_size_height, width=6)

fig_ext_num_frame = Frame(frame)

fig_ext = StringVar()
fig_ext_option_menu = apply(OptionMenu, (fig_ext_num_frame, fig_ext) + tuple([".emf", ".eps", ".pdf", ".png", ".ps", ".raw", ".rgba", ".svg", ".svgz"]))
fig_ext_option_menu.config(width=14)
fig_ext.set(".pdf")

fig_num = StringVar()
fig_num_option_menu = apply(OptionMenu, (fig_ext_num_frame, fig_num) + tuple(["1", "2", "3", "4", "5"]))
fig_num_option_menu.config(width=14)
fig_num.set("1")

fig_w_space_frame = Frame(frame)

fig_w_space = StringVar()
fig_w_space_label = Label(fig_w_space_frame, text="Fig Width Space: ")
fig_w_space_entry = Entry(fig_w_space_frame, textvariable=fig_w_space, width=6)

fig_h_space_frame = Frame(frame)

fig_h_space = StringVar()
fig_h_space_label = Label(fig_h_space_frame, text="Fig Height Space:")
fig_h_space_entry = Entry(fig_h_space_frame, textvariable=fig_h_space, width=6)

coords_frame = Frame(frame)

coords = StringVar()
coords_option_menu = apply(OptionMenu, (coords_frame, coords) + tuple(["radar", "geo"]))
coords_option_menu.config(width=15)
coords.set("geo")






map_options_label = Label(frame, text="MAP: ", anchor=W)

coastline_res_frame = Frame(frame)

coastline = IntVar()
coastline_checkbutton = Checkbutton(coastline_res_frame, text="Show Coastline", variable=coastline)

resolution = StringVar()
resolution.set("c")
resolution_option_menu = apply(OptionMenu, (coastline_res_frame, resolution) + tuple(["c", "l", "i", "h", "f", "None"]))
resolution_option_menu.config(width=15)

lalo_settings_frame = Frame(frame)

lalo_label = IntVar()
lalo_label_checkbutton = Checkbutton(lalo_settings_frame, text="Show LALO Label", variable=lalo_label)

lalo_step = StringVar()
lalo_step_label = Label(lalo_settings_frame, text="LALO Step: ")
lalo_step_entry = Entry(lalo_settings_frame, textvariable=lalo_step, width=6)

scalebar_settings = Frame(frame)

scalebar_distance = StringVar()
scalebar_lat = StringVar()
scalebar_lon = StringVar()

scalebar_label = Label(scalebar_settings, text="Scalebar")
scalebar_dist_label = Label(scalebar_settings, text="Dist: ")
scalebar_dist_entry = Entry(scalebar_settings, textvariable=scalebar_distance, width=4)
scalebar_lat_label = Label(scalebar_settings, text="Lat/Lon: ")
scalebar_lat_entry = Entry(scalebar_settings, textvariable=scalebar_lat, width=4)
scalebar_lon_entry = Entry(scalebar_settings, textvariable=scalebar_lon, width=4)

show_scalebar_frame = Frame(frame)

show_scalebar = IntVar()
show_scalebar.set(1)
show_scalebar_checkbutton = Checkbutton(show_scalebar_frame, text="Show Scalebar", variable=show_scalebar)





output_label = Label(frame, text="OUTPUT", anchor=W)
output_frame = Frame(frame)

save = IntVar()
save_checkbutton = Checkbutton(output_frame, text="Save Output", variable=save)

output_file = StringVar()
output_file_label = Label(output_frame, text="Output File: ")
output_file_entry = Entry(output_frame, textvariable=output_file, width=12)







pick_h5_file_frame.pack(anchor='w', fill=X, pady=(10, 5), padx=10)
pick_h5_file_button.pack(side=LEFT, anchor='w', padx=(0, 20))
selected_ts_file_label.pack(side=LEFT, fill=X)

pick_mask_file_frame.pack(anchor='w', fill=X)
pick_mask_file_button.pack(side=LEFT, anchor='w', pady=5, padx=(10, 20))
selected_mask_file_label.pack(side=LEFT, fill=X)

display_options_label.pack(anchor='w', fill=X, pady=(35, 0), padx=10)

y_lim_frame.pack(fill=X, pady=10, padx=10)

y_lim_upper_frame.pack(side=TOP, fill=X, pady=(0, 10))
y_lim_upper_label.pack(side=LEFT)
y_lim_upper_slider.pack(side=LEFT, padx=10)
y_lim_upper_entry.pack(side=LEFT)

y_lim_lower_frame.pack(side=TOP, fill=X)
y_lim_lower_label.pack(side=LEFT)
y_lim_lower_slider.pack(side=LEFT, padx=10)
y_lim_lower_entry.pack(side=LEFT)

unit_cmap_projection_frame.pack(anchor='w', fill=X, pady=10, padx=10)
unit_option_menu.pack(side=LEFT, padx=(0, 10))
colormap_option_menu.pack(side=LEFT, padx=(0, 10))
projection_option_menu.pack(side=LEFT)

flip_frame.pack(anchor='w', fill=X, pady=10, padx=10)
lr_flip_checkbutton.pack(side=LEFT, padx=(0, 12))
ud_flip_checkbutton.pack(side=LEFT, padx=(0, 12))
wrap_checkbutton.pack(side=LEFT, padx=(0, 12))
opposite_checkbutton.pack(side=LEFT)

transparency_frame.pack(side=TOP, fill=X)
transparency_label.pack(side=LEFT)
transparency_slider.pack(side=LEFT, padx=10)
transparency_entry.pack(side=LEFT)

show_info_checkbutton.pack(anchor='center', pady=10)

dem_options_label.pack(anchor='w', fill=X, pady=(35, 0), padx=10)

pick_dem_file_frame.pack(fill=X, pady=10)
pick_dem_file_button.pack(side=LEFT, anchor='w', pady=5, padx=(10, 20))
selected_dem_file_label.pack(side=LEFT, fill=X)

dem_options_frame.pack(anchor='w', fill=X, pady=(0, 10), padx=10)
dem_shading_checkbutton.pack(side=LEFT, padx=(0, 12))
dem_countours_checkbutton.pack(side=LEFT)

dem_countour_options.pack(anchor='w', fill=X, pady=10)

dem_countour_smoothing_frame.pack(anchor='w', side=LEFT, pady=(0, 10), padx=(20, 10))
dem_countour_smoothing_label.pack(side=TOP, pady=(0, 10), fill=X)
dem_countour_smoothing_entry.pack(side=TOP)

dem_countour_step_frame.pack(anchor='w', side=LEFT, pady=(5, 10), padx=10)
dem_countour_step_label.pack(side=TOP, pady=(0, 10), fill=X)
dem_countour_step_entry.pack(side=TOP)

subset_label.pack(anchor='w', fill=X, pady=(15, 0), padx=10)

subset_x_frame.pack(anchor='w', fill=X, pady=10, padx=10)

subset_x_from_label.pack(side=LEFT, padx=(0, 5))
subset_x_from_entry.pack(side=LEFT, padx=(0, 10))
subset_x_to_label.pack(side=LEFT, padx=(0, 5))
subset_x_to_entry.pack(side=LEFT, padx=(0, 10))

subset_y_frame.pack(anchor='w', fill=X, pady=10, padx=10)

subset_y_from_label.pack(side=LEFT, padx=(0, 5))
subset_y_from_entry.pack(side=LEFT, padx=(0, 10))
subset_y_to_label.pack(side=LEFT, padx=(0, 5))
subset_y_to_entry.pack(side=LEFT, padx=(0, 10))

subset_lat_frame.pack(anchor='w', fill=X, pady=10, padx=10)

subset_lat_from_label.pack(side=LEFT, padx=(0, 5))
subset_lat_from_entry.pack(side=LEFT, padx=(0, 10))
subset_lat_to_label.pack(side=LEFT, padx=(0, 5))
subset_lat_to_entry.pack(side=LEFT, padx=(0, 10))

subset_lon_frame.pack(anchor='w', fill=X, pady=10, padx=10)

subset_lon_from_label.pack(side=LEFT, padx=(0, 5))
subset_lon_from_entry.pack(side=LEFT, padx=(0, 10))
subset_lon_to_label.pack(side=LEFT, padx=(0, 5))
subset_lon_to_entry.pack(side=LEFT, padx=(0, 10))

reference_label.pack(fill=X, padx=10, pady=(35, 10))

ref_xy_frame.pack(anchor='w', fill=X, pady=10, padx=10)

ref_x_label.pack(side=LEFT, padx=(0, 5))
ref_x_entry.pack(side=LEFT, padx=(0, 10))
ref_y_label.pack(side=LEFT, padx=(0, 5))
ref_y_entry.pack(side=LEFT, padx=(0, 10))

ref_latlon_frame.pack(anchor='w', fill=X, pady=10, padx=10)

ref_lat_label.pack(side=LEFT, padx=(0, 5))
ref_lat_entry.pack(side=LEFT, padx=(0, 10))
ref_lon_label.pack(side=LEFT, padx=(0, 5))
ref_lon_entry.pack(side=LEFT, padx=(0, 10))

show_ref_frame.pack(anchor='w', fill=X, padx=10, pady=(0, 10))
show_ref_checkbutton.pack(side=LEFT, pady=10)

reference_options_frame.pack(anchor='w', fill=X, pady=(0, 10), padx=10)
ref_color_option_menu.pack(side=LEFT, padx=(0, 10))
ref_symbol_option_menu.pack(side=LEFT, padx=(0, 10))
ref_date_option_menu.pack(side=LEFT)

figure_label.pack(fill=X, padx=10, pady=(35, 10))

font_dpi_frame.pack(anchor='w', fill=X, padx=10, pady=10)
font_size_label.pack(side=LEFT, padx=(0, 5))
font_size_entry.pack(side=LEFT, padx=(0, 10))
dpi_label.pack(side=LEFT, padx=(0, 5))
dpi_entry.pack(side=LEFT)

row_col_num_frame.pack(anchor='w', fill=X, padx=10, pady=10)
row_num_label.pack(side=LEFT, padx=(0, 5))
row_num_entry.pack(side=LEFT, padx=(0, 10))
col_num_label.pack(side=LEFT, padx=(0, 5))
col_num_entry.pack(side=LEFT)

axis_cbar_frame.pack(anchor='w', fill=X, pady=10, padx=10)
axis_show_checkbutton.pack(side=LEFT, padx=(0, 12))
cbar_show_checkbutton.pack(side=LEFT, padx=(0, 12))
title_show_checkbutton.pack(side=LEFT, padx=(0, 12))

title_tick_frame.pack(anchor='w', fill=X, pady=10, padx=10)
tick_show_checkbutton.pack(side=LEFT, padx=(0, 12))
title_in_checkbutton.pack(side=LEFT)

title_input_frame.pack(anchor='w', fill=X, pady=10, padx=10)
title_input_label.pack(side=LEFT, padx=(0, 10))
title_input_entry.pack(side=LEFT)

fig_size_frame.pack(anchor='w', fill=X, pady=10, padx=10)
fig_size_label.pack(side=LEFT, padx=(0, 10))
fig_size_width_label.pack(side=LEFT, padx=(0, 5))
fig_size_width_entry.pack(side=LEFT, padx=(0, 10))
fig_size_height_label.pack(side=LEFT, padx=(0, 5))
fig_size_height_entry.pack(side=LEFT, padx=(0, 10))

fig_ext_num_frame.pack(anchor='w', fill=X, padx=10, pady=10)
fig_ext_option_menu.pack(side=LEFT, padx=(0, 10))
fig_num_option_menu.pack(side=LEFT, padx=(0, 10))

fig_w_space_frame.pack(anchor='w', fill=X, padx=10, pady=10)
fig_w_space_label.pack(side=LEFT, padx=(0, 5))
fig_w_space_entry.pack(side=LEFT, padx=(0, 10))

fig_h_space_frame.pack(anchor='w', fill=X, padx=10, pady=10)
fig_h_space_label.pack(side=LEFT, padx=(0, 5))
fig_h_space_entry.pack(side=LEFT)

coords_frame.pack(anchor='w', fill=X, padx=10, pady=10)
coords_option_menu.pack(side=LEFT)

map_options_label.pack(fill=X, padx=10, pady=(35, 10))

coastline_res_frame.pack(anchor='w', fill=X, padx=10, pady=10)
coastline_checkbutton.pack(side=LEFT, padx=(0, 25))
resolution_option_menu.pack(side=LEFT)

lalo_settings_frame.pack(fill=X, padx=10, pady=10)
lalo_label_checkbutton.pack(side=LEFT, padx=(0, 15))
lalo_step_label.pack(side=LEFT, padx=(0, 5))
lalo_step_entry.pack(side=LEFT)

scalebar_settings.pack(fill=X, padx=10, pady=10)
scalebar_label.pack(side=LEFT, padx=(0, 10))
scalebar_dist_label.pack(side=LEFT, padx=(0, 2))
scalebar_dist_entry.pack(side=LEFT, padx=(0, 5))
scalebar_lat_label.pack(side=LEFT, padx=(0, 2))
scalebar_lat_entry.pack(side=LEFT)
scalebar_lon_entry.pack(side=LEFT)

show_scalebar_frame.pack(fill=X, padx=10, pady=5)
show_scalebar_checkbutton.pack(side=LEFT, pady=10)

output_label.pack(anchor='w', fill=X, padx=10, pady=(35, 10))

output_frame.pack(anchor='w', fill=X, padx=10, pady=10)
save_checkbutton.pack(side=LEFT, padx=(0, 10))
output_file_label.pack(side=LEFT, padx=(0, 5))
output_file_entry.pack(side=LEFT)

space = Frame(frame)
space.config(height=50)
space.pack(side=LEFT)



mainloop()