class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy and tx != ty:
            if sx == tx and sy == ty:
                return True
            if tx < ty:
                ty %= tx
            else:
                tx %= ty
        if sx == tx and sy == ty:
            return True
        elif sx == tx:
            return ty > sy and (ty-sy) % tx == 0
        elif sy == ty:
            return tx > sx and (tx-sx) % ty == 0
        return False
