import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox,TextArea

def bar_plot_with_images(
        df_to_plot, 
        img_list, 
        xtick_labels=[], 
        orientation='v', 
        img_scale=0.15, 
        x_offset=0, 
        y_offset=0, 
        frameon=False, 
        **kwargs,
    ):


    fig, ax = plt.subplots()
    # fig = plt.figure()
    # ax  = fig.add_axes()

    if orientation.lower()=='v':
        df_to_plot.plot(
            kind='bar',
            ax=ax,
            **kwargs
        )
        ax.grid(axis='y')
    
    else:
        df_to_plot.plot(
            kind='barh',
            ax=ax,
            **kwargs
        )
        ax.grid(axis='x')


    #-- Overide AxesSubplot returned by pandas with with Matplotlib axis
    # ax = plt.gca()
    #fig, ax = plt.subplots()

    #-- Some options that can probably be commented out     
    ax.legend()
    ax.set_xticks(ticks=df_to_plot.index, labels=xtick_labels or df_to_plot.index)

    #-- Annotate each bar in the chart with an image
    for bar, img in zip(ax.patches, img_list):

        #-- get bar coordinates
        bar_x_pos = bar.get_x()
        bar_y_pos = bar.get_y()

        _x_offset = x_offset + (bar.get_width()/2)
        _y_offset = y_offset + bar.get_height()

        _x = bar_x_pos + _x_offset
        _y = bar_y_pos + _y_offset

        #-- create an annotation box container for each image
        imagebox = OffsetImage(img, zoom = img_scale)
        #imagebox.image.axes = ax
        ab = AnnotationBbox(imagebox, (_x,_y), frameon=frameon)

        ax.add_artist(ab)
        # _value:str = f"{bar.get_height():.2f}%"
        # ax.annotate(_value, (bar.get_x() * 1.005, bar.get_height() * 1.005),rotation=45)  #annotate text
        

def box_plot_with_images(
        df_to_plot, 
        img_list, 
        xtick_labels=[], 
        orientation='v', 
        img_scale=0.15, 
        x_offset=0, 
        y_offset=0, 
        frameon=False, 
        color = dict(),
        **kwargs,  
    ):

    default_color = {
        "boxes": "DarkGreen",
        "whiskers": "DarkOrange",
        "medians": "DarkBlue",
        "caps": "Gray",
    }

    color = default_color | color  #join the two dictionaries and update defaults with passed values

    if orientation.lower()=='v':
        is_vertical = True
    
    elif orientation.lower()=='h':
        is_vertical = False
    
    
    df_to_plot.plot.box(color=color, vert=is_vertical)


if __name__ == "__main__":
    pass