"""Visualization related functions.
"""
import logging
from typing import Optional, Tuple

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

import pyBigWig

from raesymatto.utils import Units

def hide_frame(ax:plt.Axes) -> None:
    """Hides spines.

    Args:
        ax (plt.Axes): Axes to be used.

    Returns:

    Raises:
    """
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')

def draw_region_information(ax:plt.Axes,chromosome:str,
                            start:int,end:int,fontsize:int=7,
                            kwargs:Optional[dict]=None) -> None:
    """Draws region information.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        fontsize (int): Font size.
        kwargs (Optional[dict]): Additional arguments passed to Axes.arrow.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'lw':0.25}

    # region text
    ax.text((end+start)*0.5,2.5,'%s:%s-%s'%(chromosome,
                                            '{:,d}'.format(start),
                                            '{:,d}'.format(end)),
            va='center',ha='center',fontsize=fontsize)

    # scale bar with the tee arrow heads
    scalebar_length = (10**(len('%.0f'%((end-start)*0.2))-1)*
                       np.round(((end-start)*0.2)/
                                10**(len('%.0f'%((end-start)*0.2))-1)))
    # arrow body
    ax.arrow(x=end-scalebar_length-0.05,y=1,
             dx=scalebar_length,dy=0,**kwargs)
    # tee arrow heads
    ax.arrow(x=end-0.05,y=1.25,dx=0,dy=-0.5,**kwargs)
    ax.arrow(x=end-scalebar_length-0.05,y=1.25,dx=0,dy=-0.5,**kwargs)

    # label the scale bar
    multiplier,prefix = (Units(
        overrides={-2:{'multiplier':1e-0,
                       'prefix':''},
                   -1:{'multiplier':1e-0,
                       'prefix':''},
                   1:{'multiplier':1e-0,
                      'prefix':''},
                   2:{'multiplier':1e-0,
                      'prefix':''}})
                         .convert(scalebar_length))
    ax.text(x=end-scalebar_length-(end-start)*0.01,
            y=1,
            s='%.0f %sb'%(multiplier,prefix),
            ha='right',va='center',fontsize=fontsize)

    ax.set_xlim(start,end)
    ax.set_ylim(0,5)
    ax.set_xticks([])
    ax.set_yticks([])

    hide_frame(ax)

def draw_bw(ax:plt.Axes,chromosome:str,start:int,end:int,
            bw:pyBigWig.pyBigWig,ymin:Optional[float]=None,
            ymax:Optional[float]=None,xspine:Optional[float]=None,
            skip:int=1,fontsize:int=7,ylabel:Optional[str]=None,
            label:Optional[str]=None,kwargs:Optional[dict]=None) -> None:
    """Draws bigWig data.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        bw (pyBigWig.pybigWig): bigWig object.
        ymin (Optional[float]): Bottom of y axis.
        ymax (Optional[float]): Top of y axis.
        xspine (Optional[float]): Location for x spine.
        skip (int): Visualize every skip-th value. Useful for downsampling.
        fontsize (int): Font size.
        ylabel (Optional[str]): Y axis label.
        label (Optional[str]): Legend label.
        kwargs (Optional[dict]): Additional arguments passed
            to Axes.fill_between.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'facecolor':'gray',
                  'alpha':1.0,
                  'lw':0.1}

    ax.fill_between(x=np.array(range(start,end))[::skip],
                    y1=bw.values(chromosome,start,end)[::skip],
                    label=label,**kwargs)

    ax.set_ylabel(ylabel,fontsize=fontsize)

    ax.set_xlim(start,end)
    ax.set_xticks([])
    ax.set_ylim(bottom=ymin,top=ymax)
    ax.tick_params(axis='y',labelsize=fontsize)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    if xspine is not None:
        ax.spines['bottom'].set_position(('data',xspine))

def draw_bed(ax:plt.Axes,chromosome:str,start:int,end:int,
             bed:pd.DataFrame,fontsize=7,label:Optional[str]=None,
             frame:bool=True,scores:bool=False,cmap:str='Greys',
             vmin:Optional[float]=None,vmax:Optional[float]=None,
             spacing:int=1,kwargs:Optional[dict]=None) -> None:
    """Draws genomics regions defined using the BED format.

    Score defines the color. Does not take into account strand
    information at the moment.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        bed (pd.DataFrame): Data in Browser Extensible Data (BED) format.
        fontsize (int): Font size.
        label (Optional[str]): Y axis label.
        frame (bool): Draw spines.
        scores (bool): Color the BED lines.
        cmap (str): Colormap to be used when coloring the BED lines.
        vmin (Optional[float]): Minimum score.
        vmax (Optional[float]): Maximum score.
        spacing (int): Spacing between rows of elements.
        kwargs (Optional[dict]): Additional arguments passed
            to mpl.patches.Rectangle.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'facecolor':'gray',
                  'edgecolor':'gray',
                  'alpha':1.0,
                  'lw':0.0}

    def distribute_intervals(intervals):
        levels = []
        for interval_idx in range(0,intervals.shape[0]):
            found_place = False
            for level_idx in range(0,len(levels)):
                if levels[level_idx][-1][2] < intervals[interval_idx][1]:
                    levels[level_idx].append(intervals[interval_idx])
                    found_place = True
                    break
            if not found_place:
                levels.append([intervals[interval_idx]])
        return levels

    intervals = (bed[(bed.iloc[:,0] == chromosome) &
                     (((bed.iloc[:,1] >= start) &
                       (bed.iloc[:,1] <= end)) |
                     ((bed.iloc[:,2] >= start) &
                      (bed.iloc[:,2] <= end)) |
                     ((start >= bed.iloc[:,[1,2]].min(axis=1)) &
                      (end <= bed.iloc[:,[1,2]].max(axis=1))))].values)

    if intervals.shape[0] > 0:
        intervals = intervals[np.lexsort((-(intervals[:,2]-
                                            intervals[:,1]),
                                          intervals[:,1])),:]

    levels = distribute_intervals(intervals)

    if intervals.shape[0] > 0 and scores:
        if vmin is None:
            vmin = intervals[:,4].min()
        if vmax is None:
            vmax = intervals[:,4].max()

        norm = mpl.colors.Normalize(vmin=vmin,vmax=vmax)
        color = mpl.cm.get_cmap(cmap)

        # if score == True, then user-specified facecolor
        # or fc should not be used
        if 'facecolor' in kwargs or 'fc' in kwargs:
            logging.warning('facecolor/fc removed from kwargs '
                            'as scores == True')
            kwargs.pop('facecolor',None)
            kwargs.pop('fc',None)

    for idx,level in enumerate(levels):
        for region in level:
            if not scores:
                rect = mpl.patches.Rectangle(xy=(region[1],spacing*idx-0.25),
                                             width=region[2]-region[1],
                                             height=0.5,**kwargs)
            else:
                # get the color of the current region
                kwargs['facecolor'] = color(norm(region[4]))
                rect = mpl.patches.Rectangle(xy=(region[1],spacing*idx-0.25),
                                             width=region[2]-region[1],
                                             height=0.5,
                                             **kwargs)
            ax.add_patch(rect)

    if len(levels) > 0:
        ax.set_ylim(-0.5,spacing*(len(levels)-1)+0.5)
    else:
        logging.warning('No regions found!')

    ax.set_ylabel(label,fontsize=fontsize)

    ax.set_xlim(start,end)
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.set_xticks([])
    ax.set_yticks([])

    if not frame:
        hide_frame(ax)

def draw_boxes(ax:plt.Axes,chromosome:str,start:int,end:int,
               bed:pd.DataFrame,fontsize:int=7,
               ylabel:Optional[dict]=None,vmin:Optional[float]=None,
               vmax:Optional[float]=None,kwargs:Optional[dict]=None) -> None:
    """Draws genomics regions defined using the BED format.

    Score defines the height. Does not take into account strand
    information at the moment.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        bed (pd.DataFrame): Data in Browser Extensible Data (BED) format.
        fontsize (int): Font size.
        ylabel (Optional[str]): Y axis label.
        vmin (Optional[float]): Minimum score.
        vmax (Optional[float]): Maximum score.
        kwargs (Optional[dict]): Additional arguments passed
            to mpl.patches.Rectangle.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'facecolor':'gray',
                  'edgecolor':'gray',
                  'alpha':1.0,
                  'lw':0.0}

    intervals = (bed[(bed.iloc[:,0] == chromosome) &
                     (((bed.iloc[:,1] >= start) &
                       (bed.iloc[:,1] <= end)) |
                      ((bed.iloc[:,2] >= start) &
                       (bed.iloc[:,2] <= end)) |
                      ((start >= bed.iloc[:,[1,2]].min(axis=1)) &
                       (end <= bed.iloc[:,[1,2]].max(axis=1))))])

    for _,interval in intervals.iterrows():
        rect = mpl.patches.Rectangle(xy=(interval.iloc[1],0),
                                     width=(interval.iloc[2]-
                                            interval.iloc[1]),
                                     height=interval.iloc[4],
                                     **kwargs)
        ax.add_patch(rect)

    if intervals.shape[0] > 0:
        ax.set_ylim(bottom=0,top=intervals.iloc[:,4].max())

    ax.set_ylabel(ylabel,fontsize=fontsize)

    ax.set_xlim(start,end)
    ax.set_ylim(bottom=vmin,top=vmax)
    ax.set_xticks([])

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

def draw_loops(ax:plt.Axes,chromosome:str,start:int,end:int,
               bed:pd.DataFrame,fontsize:int=7,
               ymin:float=1,ymax:float=10,flip:bool=False,
               frame:bool=True,ylabel:Optional[str]=None,
               kwargs:Optional[dict]=None) -> None:
    """Draws loops.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        bed (pd.DataFrame): Data in Browser Extensible Data (BED) format.
        fontsize: Font size.
        ymin (float): Minimum loop height.
        ymax (float): Maximum loop height.
        flip (bool): Flip the y axis.
        frame (bool): Draw spines.
        ylabel (Optional[str]): Y axis label.
        kwargs (Optional[dict]): Additional arguments passed
            to mpl.patches.PathPatch.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'lw':0.5,
                  'ec':'red',
                  'fc': 'none',
                  'alpha':1.0}

    intervals = bed[(bed.iloc[:,0] == chromosome) &
                    (((bed.iloc[:,1] >= start) &
                      (bed.iloc[:,1] <= end)) |
                     ((bed.iloc[:,2] >= start) &
                      (bed.iloc[:,2] <= end)) |
                     ((start >= bed.iloc[:,[1,2]].min(axis=1)) &
                      (end <= bed.iloc[:,[1,2]].max(axis=1))))].values

    length_max = (intervals[:,2]-intervals[:,1]).max()

    Path = mpl.path.Path
    for interval in intervals:
        pp = (mpl.patches
              .PathPatch(Path([(interval[1],0),
                               ((interval[1]+interval[2])/2,
                                max([ymin,2.0*ymax*
                                     (interval[2]-interval[1])/
                                     length_max])),
                               (interval[2],0)],[Path.MOVETO,
                                                 Path.CURVE3,
                                                 Path.CURVE3]),
                         transform=ax.transData,
                         **kwargs))
        ax.add_patch(pp)

    ax.set_ylabel(ylabel,fontsize=fontsize)

    ax.set_xlim([start,end])
    ax.set_ylim([0,ymax*1.05])
    ax.set_xticks([])
    ax.set_yticks([])

    if flip:
        ax.invert_yaxis()

    if not frame:
        hide_frame(ax)

def draw_gene_models(ax:plt.Axes,chromosome:str,start:int,end:int,
                     genes:pd.DataFrame,min_height:int=None,
                     gene_name_field:str='gene_id',fontsize:int=7,
                     frame:bool=True,kwargs:Optional[dict]=None) -> None:
    """Draws gene models.

    Args:
        ax (plt.Axes): Axes to be used.
        chromosome (str): Chromosome of interest.
        start (int): Start coordinate.
        end (int): End coordinate.
        genes (pd.DataFrame): Gene definitions in General Transfer
            Format (GTF).
        min_height (Optional[int]): Minimum number of gene tracks.
            This can be used to have predictable gene heights.
        gene_name_field (str): Name of the column to be used
            when labeling genes.
        fontsize (int): Font size.
        frame (bool): Draw spines.
        kwargs (Optional[dict]): Additional arguments passed to Axes.text.

    Returns:

    Raises:
    """
    if kwargs is None:
        kwargs = {'ha':'center',
                      'va':'center',
                      'fontsize':fontsize,
                      'style':'italic'}

    def draw_name(ax:plt.Axes,position:Tuple[float,float],
                  name:str,kwargs:Optional[dict]=None) -> None:
        """Draws gene name.

        Args:
            ax (matplotlib.pyplot.axis): Axes to be used.
            position (Tuple[float,float]): Position.
            name (str): Name.
            kwargs (dict): Additional arguments passed to Axes.text.
        """
        if kwargs is None:
            kwargs = {'ha':'center',
                      'va':'center',
                      'fontsize':fontsize,
                      'style':'italic'}

        ax.text(position[0],position[1],
                name,**kwargs)

    def draw_rectangle(ax:plt.Axes,xy:Tuple[float,float],
                       width:float,height:float,
                       kwargs:Optional[dict]=None) -> None:
        """Draws rectangle.

        Args:
            ax (plt.Axes): Axes to be used.
            xy (Tuple[float,float]): The anchor point.
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
            kwargs (Optional[dict]): Additional arguments
                passed to mpl.patch.Rectangle.

        Returns:

        Raises:
        """
        if kwargs is None:
            kwargs = {'linewidth':0,
                      'edgecolor':'k',
                      'facecolor':'k'}

        rectangle = mpl.patches.Rectangle(xy=xy,
                                          width=width,
                                          height=height,
                                          **kwargs)
        ax.add_patch(rectangle)

    tmp = (genes[['transcript_id','seqname','start','end']]
           .groupby(['transcript_id','seqname'])
           .agg({'start':'min','end':'max'})
           .reset_index())

    # transcripts completely within in the region of interest
    tmp = tmp[(tmp['seqname']== chromosome) &
              ((start >= tmp['start']) &
               (end <= tmp['end']))]['transcript_id'].values

    # transcripts partially within in the region of interest
    tmp2 = genes[(genes['seqname'] == chromosome) &
            (((genes['start'] >= start) &
              (genes['start'] <= end)) |
             ((genes['end'] >= start) &
              (genes['end'] <= end)))]['transcript_id'].values

    transcript_ids = np.union1d(tmp,tmp2)

    for n,transcript_id in enumerate(transcript_ids):

        pieces = genes[genes['transcript_id'] == transcript_id]
        tmp = genes[genes['transcript_id'] == transcript_id]

        draw_rectangle(ax,(tmp['start'].min(),n-0.025),
                       tmp['start'].max()-tmp['start'].min(),
                       0.05)

        # draw arrow heads to represent the directionality
        current_position = (max(tmp['start'].min(),start)+
                            0.01*(end-start))
        while current_position <= min(end,tmp['start'].max()):
            if tmp['strand'].iloc[0] == '+':
                ax.plot([current_position-0.002*(end-start),
                         current_position,
                         current_position-0.002*(end-start)],
                        [n+0.125,n,n-0.125],
                        lw=0.1,c='k')
            elif tmp['strand'].iloc[0] == '-':
                ax.plot([current_position+0.002*(end-start),
                         current_position,
                         current_position+0.002*(end-start)],
                        [n+0.125,n,n-0.125],
                        lw=0.1,c='k')
            current_position += 0.01*(end-start)

        # draw gene name
        # fits the region of interest
        if tmp['start'].min() > start and tmp['end'].max() < end:
            draw_name(ax,((tmp['end'].max()+tmp['start'].min())*0.5,
                          n-0.5),
                      pieces[gene_name_field].iloc[0],kwargs)
        else: # does not fit the region of interest
            if tmp['strand'].iloc[0] == '+':
                if (tmp['start'].min() <= start and
                    tmp['end'].max() >= end):
                    draw_name(ax,((end+start)*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)
                elif tmp['start'].min() <= start:
                    draw_name(ax,((tmp['end'].max()+start)*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)
                elif tmp['start'].max() >= end:
                    draw_name(ax,((end+tmp['start'].min())*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)
            else:
                if (tmp['end'].min() <= start and
                    tmp['start'].max() >= end):
                    draw_name(ax,((end+start)*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)
                elif tmp['start'].max() < end:
                    draw_name(ax,((tmp['start'].max()+start)*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)
                elif tmp['end'].min() > start:
                    draw_name(ax,((end+tmp['end'].min())*0.5,n-0.5),
                              pieces[gene_name_field].iloc[0],kwargs)

        # draw exons and CDSs
        for _,piece in pieces.iterrows():
            if piece['feature'] == 'exon':
                draw_rectangle(ax,(piece['start'],n-0.125),
                               piece['end']-piece['start'],
                               0.25)
            elif piece['feature'] == 'CDS':
                draw_rectangle(ax,(piece['start'],n-0.25),
                               piece['end']-piece['start'],
                               0.5)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(start,end)
    if min_height is not None:
        if min_height < len(transcript_ids):
            logging.warning(('%d genes would not be visible due '
                             'to min_height=%d, discard min_height.'),
                            len(transcript_ids)-min_height,min_height)
            ax.set_ylim(-0.5,min(len(transcript_ids),1)-0.5)
        else:
            ax.set_ylim(-(min_height-len(transcript_ids))-0.5,
                        len(transcript_ids)-0.5)
    else:
        ax.set_ylim(-0.5,min(len(transcript_ids),1)-0.5)

    if not frame:
        hide_frame(ax)
        