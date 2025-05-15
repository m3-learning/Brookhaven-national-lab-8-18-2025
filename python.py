import torch
import torch.nn.functional as F

def radial_weighted_loss(
    pred,
    target,
    center,
    areal_density_fn=torch.exp,
    loss_fn=F.mse_loss,
    reduction="mean",
):
    """
    Weighted loss based on areal density from the center of a circle.

    Parameters:
    - pred: [B, 1, H, W]
    - target: [B, 1, H, W]
    - center: tuple of (y_c, x_c)
    - areal_density_fn: callable applied to radial distance tensor
    - loss_fn: pointwise loss function (e.g., mse, l1)
    - reduction: 'mean' or 'sum'

    Returns:
    - scalar loss
    """
    B, C, H, W = pred.shape
    y = torch.arange(H, device=pred.device).view(1, H, 1).expand(1, H, W)
    x = torch.arange(W, device=pred.device).view(1, 1, W).expand(1, H, W)

    y_c, x_c = center
    r = torch.sqrt((x - x_c) ** 2 + (y - y_c) ** 2)  # [1, H, W]

    # Normalize if desired
    r = r / r.max()

    # Compute weight map
    weights = areal_density_fn(-(r**2))  # e.g. Gaussian profile

    # Expand weights to [B, 1, H, W]
    weights = weights.unsqueeze(0).unsqueeze(0)

    # Compute loss per pixel
    pointwise_loss = loss_fn(pred, target, reduction="none")

    # Weighted sum
    weighted = pointwise_loss * weights

    if reduction == "mean":
        return weighted.sum() / weights.sum()
    elif reduction == "sum":
        return weighted.sum()
    else:
        return weighted  # no reduction
