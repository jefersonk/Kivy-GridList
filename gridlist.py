class GridListView(ListView):
    def __init__(self, **kwargs):
        super(GridListView, self).__init__(**kwargs)

    def populate(self, istart=None, iend=None):
        """
        It was overwritten the method to correct height
        :param istart:
        :param iend:
        :return:
        """
        container = self.container
        sizes = self._sizes
        rh = self.row_height

        if istart is None:
            istart = self._wstart
            iend = self._wend

        # clear the view
        container.clear_widgets()

        if iend is not None and iend != -1:

            # fill with a "padding"
            fh = 0
            for x in range(istart):
                fh += sizes[x] if x in sizes else rh

            # now fill with real item_view
            index = istart
            while index <= iend:
                item_view = self.adapter.get_view(index)
                index += 1
                if item_view is None:
                    continue
                sizes[index] = item_view.height
                container.add_widget(item_view)

        else:
            available_height = self.height
            real_height = 0
            index = self._index
            count = 0
            while available_height > 0:
                item_view = self.adapter.get_view(index)
                if item_view is None:
                    break
                sizes[index] = item_view.height
                index += 1
                count += 1
                container.add_widget(item_view)
                available_height -= item_view.height
                real_height += item_view.height + 10

            self._count = count

            columns = int(self.width / self.adapter.get_view(0).width)
            multiply = float(float(self.adapter.get_count()) / columns)
            if multiply > int(multiply):
                multiply += 1

            if count:
                self.container.height = \
                    real_height / count * int(multiply)
                if self.row_height is None:
                    self.row_height = real_height / count

            self.populate(istart=0, iend=self.adapter.get_count())

    def _scroll(self, scroll_y):
        if self.row_height is None:
            return
        self._scroll_y = scroll_y
        scroll_y = 1 - min(1, max(scroll_y, 0))
        container = self.container
        mstart = (container.height - self.height) * scroll_y
        mend = mstart + self.height

        # convert distance to index
        columns = int(self.width / self.adapter.get_view(0).width)
        rh = self.row_height / columns
        istart = int(ceil(mstart / rh))
        iend = int(floor(mend / rh))

        istart = max(0, istart - 1)
        iend = max(0, iend - 1)

        if (iend + 10) > self._count:
            iend = self._count - 10

        if istart < self._wstart:
            rstart = max(0, istart - 10)
            self.populate(rstart, iend)
            self._wstart = rstart
            self._wend = iend
        elif iend > self._wend:
            self.populate(istart, iend + 10)
            self._wstart = istart
            self._wend = iend + 5

    def do_layout(self, *largs):
        super(GridListView, self).do_layout(*largs)
        self.populate(istart=-1)
